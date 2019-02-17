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
			return round(sum(self.intervals),1)
		else:
			self.intervals[-1] += time.time() - self.lastFlag
			self.stopped = True
			return round(sum(self.intervals),1)
	def NewInterval(self):
		if self.stopped:
			self.intervals.append(0)
		else:
			self.Stop()
			self.Start()
			self.intervals.append(0)
		return round(self.intervals[-2],1)
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
		return round(average,1)
		
if __name__ == "__main__":
	sw = StopWatch()
	sw.Start()
	time.sleep(5)
	t = sw.Stop()
	print("Time passed is " + str(t) + " seconds")
	print("clearing...")
	sw.Clear()
	print("cleared!")
	sw.Start()
	time.sleep(2)
	i = sw.NewInterval()
	print("Last interval was " + str(i) + " seconds")
	time.sleep(3)
	t = sw.Stop()
	print("Total time passed since clearing is " + str(t) + " seconds")
	avg = sw.AverageIntervalTime()
	i = sw.NewInterval()
	print("Last interval was " + str(i) + " seconds")
	print("Average interval time is " + str(avg))
	time.sleep(2)
	