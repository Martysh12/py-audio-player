import curses
import _curses

import pygame

from time import strftime, gmtime
import sys
import os

pygame.mixer.init()

BORDER_CHARS = { # │ ─ ┌ ┬ ┐ ├ ┼ ┤ └ ┴ ┘
	"flat"	: {
		"vertical"   : "│",
		"horizontal" : "─",
	},

	"corners" : {
		"down_right" : "┌",
		"down_left"  : "┐",
		"up_right"   : "└",
		"up_left"	: "┘",
 	},

	"half_crosses" : {
		"vertical_right"  : "├",
		"vertical_left"   : "┤",
		"horizontal_down" : "┬",
		"horizontal_up"   : "┴",
	},

	"cross"   : "┼"
}

def main(stdscr):
	stdscr.nodelay(True)
	curses.curs_set(False)

	current_file = sys.argv[1]
	name = os.path.basename(current_file)

	stopped = True
	is_paused = True

	snd = pygame.mixer.Sound(current_file)
	chn = pygame.mixer.Channel(1)

	snd_length = snd.get_length()

	while True:
		lines, cols = stdscr.getmaxyx()
		
		# Creating a square border around the screen
		stdscr.addstr(0, 0, BORDER_CHARS["corners"]["down_right"] + (BORDER_CHARS["flat"]["horizontal"] * (cols - 2)) + BORDER_CHARS["corners"]["down_left"])
		
		for i in range(1, lines - 1):
			stdscr.addstr(i, 0, BORDER_CHARS["flat"]["vertical"].ljust(cols - 1) + BORDER_CHARS["flat"]["vertical"])

		# Using insstr because addstr fails when trying to place a character at the bottom right corner
		stdscr.insstr(lines - 1, 0, BORDER_CHARS["corners"]["up_right"] + (BORDER_CHARS["flat"]["horizontal"] * (cols - 2)) + BORDER_CHARS["corners"]["up_left"])



		# Adding sound metadata
		# Name
		stdscr.addstr(2, 2, name.center(cols - 4))
		stdscr.addstr(2, 2, "Currently playing:")

		# Duration
		if snd_length > 60:
			if snd_length > 3600:
				stdscr.addstr(3, 2, strftime("%H hours, %M minutes and %S seconds", gmtime(snd_length)).center(cols - 4))
			else:
				stdscr.addstr(3, 2, strftime("%M minutes and %S seconds", gmtime(snd_length)).center(cols - 4))
		else:
			stdscr.addstr(3, 2, strftime("%S seconds", gmtime(snd_length)).center(cols - 4))
		stdscr.addstr(3, 2, "Duration:")



		# Adding instructions
		stdscr.addstr(lines - 2, 2, "SPACE to pause/unpause, S to stop, Q to quit.")



		stdscr.refresh()

		try:
			key = stdscr.getch()
		except _curses.ERR:
			continue

		if key == ord(' '):
			if is_paused:
				if stopped:
					chn.play(snd)
					stopped = False
				else:
					chn.unpause()
			else:
				chn.pause()

			is_paused = not is_paused

		if key == ord('s'):
			is_paused = True
			stopped = True
			chn.stop()

		if key == ord('q'):
			chn.stop()
			break


curses.wrapper(main)
