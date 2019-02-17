import random
import copy

fullBlock = chr(9608)*2
emptyBlock = chr(9617)*2
mineSymbol = chr(9604)
gap = "  "

class Environment:
	def __init__(self,height = 9,width = 9,numberOfMines = 10):
		self.height					= height
		self.width					= width
		self.numberOfMines			= numberOfMines
		self.mine					= -1
		self.empty					= 0
		self.mapGenerated			= False
		self.score					= 0
		self.maxScore				= width*height-numberOfMines
		self.graphicalCellWidth		= max(len(str(width))+1,2)
		self.graphicalLeftMargin	= max(len(str(height))+2,3)
		
		self.GenerateMap((0,0))
		self.GenerateUserMap()
		
	def GetHeight(self):
		return self.height
		
	def GetEmptyCellsLeft(self):
		return self.maxScore - self.score
	
	def GetScore(self):
		return self.score
		
	def GetMaxScore(self):
		return self.maxScore
		
	def GetWidth(self):
		return self.width
	
	def GetNumberOfMines(self):
		return self.numberOfMines
		
	def GenerateUserMap(self):
		self.userMap = [[False for j in range(self.width)] for i in range(self.height)]
		
	def Click(self,x,y):
		x -= 1
		y -= 1
		if not self.mapGenerated:
			self.GenerateMap((x,y))
			self.mapGenerated = True
		activationQueue = [(x,y)]
		while len(activationQueue)>0:
			position = activationQueue.pop()
			alive = self.PositionActivation(position,activationQueue)
		return alive
		
	def PositionActivation(self,position,activationQueue):
		x = position[0]
		y = position[1]
		if self.map[x][y]==self.mine:
			return False
		if not self.userMap[x][y]:
			self.userMap[x][y] = True
			self.score += 1
			if self.map[x][y] == 0:
				xValues, yValues = self.GetWindow(x,y)
				for j in xValues:
					for i in yValues:
						if not self.userMap[j][i]:
							newPosition = (j,i)
							if not newPosition in activationQueue:
								activationQueue.append(newPosition)
		return True
		
	def GetWindow(self,x,y):
		windowXMin = max(0,x-1)
		windowXMax = min(self.height-1,x+1)
		windowYMin = max(0,y-1)
		windowYMax = min(self.width-1,y+1)
		
		xValues = set([windowXMin,x,windowXMax])
		yValues = set([windowYMin,y,windowYMax])
		return xValues, yValues
	
	def GenerateMap(self,firstClick):
		self.map =[[0 for j in range(self.width)] for i in range(self.height)]
		placedMines = 0
		while placedMines <self.numberOfMines:
			mineX, mineY = self.GetRandomPosition()
			if (not self.map[mineX][mineY]==self.mine) and (not (mineX,mineY)==firstClick):
				self.map[mineX][mineY] = self.mine
				placedMines += 1
		for i in range(self.height):
			for j in range(self.width):
				if not self.map[i][j]==self.mine:
					self.map[i][j] = self.CountNeighbouringMines(i,j)
	
	def CountNeighbouringMines(self,x,y):
		numberOfNeighbouringMines = 0
		
		xValues, yValues = self.GetWindow(x,y)
		
		for j in xValues:
			for i in yValues:
				if self.map[j][i] == self.mine:
					numberOfNeighbouringMines +=1
		return numberOfNeighbouringMines
	
	def GetRandomPosition(self):
		X = random.randint(0,self.height-1)
		Y = random.randint(0,self.width-1)
		return X, Y
		
	
	def DisplayUserMap(self):
		dispString = ""
		dispString += self.GenerateTopRowString()
		for i in range(self.height):
			dispString += self.GenerateRowString(i)
		print(dispString)
		
	def DisplayFullMap(self):
		tmpUserMap = copy.deepcopy(self.userMap)
		for i in range(self.height):
			for j in range(self.width):
				self.userMap[i][j] = True
		self.DisplayUserMap()
		self.userMap = tmpUserMap
		
	def GenerateTopRowString(self):
		topRowString = " "*self.graphicalLeftMargin
		for i in range(self.width):
			numberString = str(i+1) + ")"
			cellString = self.GenerateCellString(numberString)
			topRowString += cellString + gap
		topRowString += "\n"
		return topRowString
		
	def GenerateCellString(self,contentString):
		contentStringLength = len(contentString)
		spacingString = " "*(self.graphicalCellWidth-contentStringLength)
		cellString = contentString + spacingString
		return cellString
		
	def GenerateLeftMargin(self,contentString):
		contentStringLength = len(contentString)
		spacingString = " "*(self.graphicalLeftMargin-contentStringLength)
		marginString = contentString + spacingString
		return marginString
	
	def GenerateRowString(self,i):
		rowString = ""
		indexString = str(i+1) + ")"
		rowString += self.GenerateLeftMargin(indexString)
		
		row = self.map[i]
		for j in range(self.width):
			if self.userMap[i][j]:
				cell = row[j]
				if cell == 0:
					rowString += self.GenerateCellString(emptyBlock) + gap
				elif cell == self.mine:
					rowString += self.GenerateCellString(mineSymbol) + gap
				else:
					rowString += self.GenerateCellString(str(cell)) + gap
			else:
				rowString += self.GenerateCellString(fullBlock) + gap
		rowString += "\n\n"
		return rowString
	
	
		

if __name__ == "__main__":
	environment()