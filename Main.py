from Environment import Environment
from StopWatch import StopWatch
import os
import numpy as np

highScoreDirectory = "HighScore"

def clear():
	os.system('cls')

class MainClass:
	def __init__(self):
		self.Run()
		
	def Run(self):
		sw = StopWatch()
		clear()
		self.PromptForCustomization()
		playing = True
		while playing:
			alive = True
			gameStarted = False
			
			environment = Environment(self.height,self.width,self.numberOfMines)
			clear()
			environment.DisplayUserMap()
			while alive and (environment.GetEmptyCellsLeft()>0 or not environment.mapGenerated):
				print("Number of uncleared empty tiles: " + str(environment.GetEmptyCellsLeft()))
				x = self.SelectRow()
				y = self.SelectColumn()
				if not gameStarted:
					sw.Clear()
					sw.Start()
					gameStarted = True
				alive = environment.Click(x,y)
				clear()
				environment.DisplayUserMap()
			clear()
			environment.DisplayFullMap()
			roundTime = sw.Stop()
			if alive:
				self.WinningEvent(roundTime)
			else:
				self.LosingEvent()
			self.AskIfPlayAgain()
		
	def AskIfPlayAgain(self):
		while True:
				playAgain = (input("Do you want to play again? y/n ")).lower()
				if playAgain == "y":
					break
				elif playAgain == "n":
					playing = False
					self.ShutDown()
				else:
					self.InvalidResponseMessage()
	
	def ShutDown(self):
		print("Good bye!")
		exit()
		
		
	def WinningEvent(self,roundTime):
		print("You won!")
		print("Your time: " + str(roundTime) + " seconds")
		self.CompareToHighScore(roundTime)
				
	def LosingEvent(self):
		print("You lost!")
	
	def PromptForCustomization(self):
		while True:
			customization = (input("Do you want to customize the map? y/n ")).lower()
			if customization == "y":
				self.CustomizeParameters()
				break
			elif customization == "n":
				self.SetParametersToDefault()
				break
			else:
				self.InvalidResponseMessage()
	
	def InvalidResponseMessage(self):
		print("Invalid response!")
	
	def CompareToHighScore(self,roundTime):
		bestTimeBeaten = False
		if not os.path.isdir(highScoreDirectory):
			os.system("mkdir" + " \"" + highScoreDirectory + "\"")
		filePath = self.GetHighScoreFilePath()
		if os.path.exists(filePath):
			bestTime = np.load(filePath)
			bestTimeBeaten = bestTime > roundTime
		else:
			bestTimeBeaten = True
		if bestTimeBeaten:
			print("New HighScore!")
			np.save(filePath,roundTime)
		else:
			print("HighScore: " + str(bestTime) + " seconds")
			
		
		
	def GetHighScoreFilePath(self):
		dims = [self.height,self.width]
		dims.sort()
		filePath = highScoreDirectory + "\\" + str(dims[0]) + "X" + str(dims[1]) + "m" + str(self.numberOfMines) + "highScore.npy"
		return filePath
	
	def SelectRow(self):
		while True:
			xString = input("Select row: ")
			try:
				x = int(xString)
				if x > self.height or x<1:
					print("out of bounds")
				else:
					break
			except:
				self.InvalidResponseMessage()
		return x
		
	def SelectColumn(self):
		while True:
			yString = input("Select column: ")
			try:
				y = int(yString)
				if y > self.width or y<1:
					print("out of bounds")
				else:
					break
			except:
				self.InvalidResponseMessage()
		return y
			
			
	def CustomizeParameters(self):
		self.CustomizeHeight()
		self.CustomizeWidth()
		self.CustomizeNumberOfMines()
				
	def CustomizeHeight(self):
		while True:
			heightString = input("Enter height: ")
			try:
				self.height = int(heightString)
				if self.height < 1:
					print("Too small height!")
				else:
					break
			except:
				print("Invalid input!")
	
	def CustomizeWidth(self):
		while True:
			widthString = input("Enter width: ")
			try:
				self.width = int(widthString)
				if self.width < 1:
					print("Too small width!")
				else:
					break
			except:
				self.InvalidResponseMessage()
	
	def CustomizeNumberOfMines(self):
		while True:
			numberOfMinesString = input("Enter number of mines: ")
			try:
				self.numberOfMines = int(numberOfMinesString)
				if self.numberOfMines < 1:
					print("Too few mines!")
				elif self.numberOfMines >= self.width*self.height:
					print("Too many mines!")
				else:
					break
			except:
				self.InvalidResponseMessage()
				
	def SetParametersToDefault(self):
		environment = Environment()
		self.height = environment.GetHeight()
		self.width	= environment.GetWidth()
		self.numberOfMines = environment.GetNumberOfMines()
		
		
if __name__ == "__main__":
	MainClass()