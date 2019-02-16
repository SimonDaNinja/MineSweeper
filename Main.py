from Environment import Environment
from StopWatch import StopWatch
import os
import numpy as np

highScoreDirectory = "HighScore"

def clear():
	os.system('cls')

class MainClass:
	def __init__(self):
		clear()
		while True:
			customization = (input("Do you want to customize the map? y/n ")).lower()
			if customization == "y":
				self.useCustomParameters = True
				self.CustomizeParameters()
				break
			elif customization == "n":
				self.useCustomParameters = False
				self.SetParametersToDefault()
				break
			else:
				self.InvalidResponseMessage()
		self.Run()
		
	def InvalidResponseMessage(self):
		print("Invalid response!")
		
	def Run(self):
		sw = StopWatch()
		playing = True
		while playing:
			alive = True
			gameStarted = False
			
			self.environment = Environment(self.height,self.width,self.numberOfMines)
			clear()
			self.environment.DisplayUserMap()
			while alive and (self.environment.GetScore()<self.environment.GetMaxScore() or not self.environment.mapGenerated):
				x = self.SelectRow()
				y = self.SelectColumn()
				if not gameStarted:
					sw.Clear()
					sw.Start()
					gameStarted = True
				alive = self.environment.Click(x,y)
				clear()
				self.environment.DisplayUserMap()
			clear()
			self.environment.DisplayFullMap()
			if alive:
				print("You won!")
				roundTime = sw.Stop()
				print("Your time: " + str(roundTime) + " seconds")
				self.CompareToHighScore(roundTime)
			else:
				print("You lost!")
			while True:
				playAgain = (input("Do you want to play again? y/n ")).lower()
				if playAgain == "y":
					break
				elif playAgain == "n":
					playing = False
					break
				else:
					self.InvalidResponseMessage()
		print("Good bye!")
			
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
		filePath = highScoreDirectory + "\\" + "h" + str(self.height) + "w" + str(self.width) + "m" + str(self.numberOfMines) + "highScore.npy"
		return filePath
	
	def SelectRow(self):
		while True:
			xString = input("Select row: ")
			try:
				x = int(xString)
				if x > self.environment.GetHeight() or x<1:
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
				if y > self.environment.GetWidth() or y<1:
					print("out of bounds")
				else:
					break
			except:
				self.InvalidResponseMessage()
		return y
			
			
	def CustomizeParameters(self):
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