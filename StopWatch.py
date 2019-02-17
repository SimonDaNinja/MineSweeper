import time
class StopWatch:
	def __init__(self):
		self.lastFlag = time.time()
		self.intervals = [0]
		self.stopped = True
	def Start(self):
		if self.stopped:
			self.lastFlag = time.time()
			self.stopped = False
		else:
			pass
	def Stop(self):
		if self.stopped:
			return sum(self.intervals)
		else:
			self.intervals[-1] += time.time() - self.lastFlag
			self.stopped = True
			return sum(self.intervals)
	def NewInterval(self):
		if self.stopped:
			self.intervals.append(0)
		else:
			self.Stop()
			self.Start()
			self.intervals.append(0)
		return self.intervals[-2]
	def Clear(self):
		self.lastFlag = time.time()
		self.intervals = [0]
		self.stopped = True
	def AverageIntervalTime(self):
		if self.stopped:
			average = sum(self.intervals)/len(self.intervals)
		else:
			self.Stop()
			average = sum(self.intervals)/len(self.intervals)
			self.Start()
		return average
		
if __name__ == "__main__":
	sw = StopWatch()
	sw.Start()
	time.sleep(5)
	t = sw.Stop()
	print("Time passed is " + str(t))