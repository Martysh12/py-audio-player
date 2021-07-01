import time

class Watch:
	def __init__(self):
		self.start_time = 0
		self.time_paused = 0
		self.pause_start = 0
		self.paused_at = 0

		self.paused = True
		self.stopped = True

	def start(self):
		self.start_time = time.time()
		self.paused = False
		self.stopped = False

	def pause(self):
		self.pause_start = time.time()
		self.paused_at = self.get_time()
		self.paused = True

	def unpause(self):
		self.time_paused += time.time() - self.pause_start
		self.paused = False

	def stop(self):
		self.start_time = 0
		self.time_paused = 0
		self.paused_at = 0

		self.stopped = True
		self.paused = True

	def get_time(self):
		if self.stopped:
			return 0

		if self.paused:
			return self.paused_at

		return (time.time() - self.start_time) - self.time_paused
