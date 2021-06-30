import curses

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
	lines, cols = stdscr.getmaxyx()
	
	# Creating a square border around the screen
	stdscr.addstr(0, 0, BORDER_CHARS["corners"]["down_right"] + (BORDER_CHARS["flat"]["horizontal"] * (cols - 2)) + BORDER_CHARS["corners"]["down_left"])
	
	for i in range(1, lines - 1):
		stdscr.addstr(i, 0, BORDER_CHARS["flat"]["vertical"].ljust(cols - 1) + BORDER_CHARS["flat"]["vertical"])

	# Using insstr because addstr fails when trying to place a character at the bottom right corner
	stdscr.insstr(lines - 1, 0, BORDER_CHARS["corners"]["up_right"] + (BORDER_CHARS["flat"]["horizontal"] * (cols - 2)) + BORDER_CHARS["corners"]["up_left"])



	stdscr.getkey()

curses.wrapper(main)
