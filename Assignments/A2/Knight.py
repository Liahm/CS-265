#!/usr/bin/env python
#Eric Lee
#Info derived from https://en.wikipedia.org/wiki/Knight%27s_tour
import random
import sys
import os


#Using brackets because I am used to them
class Move: #Class for move
#{
	def __init__(self):
	#{
		self.x = 0
		self.y = 0
	#}
#}
#-----------------------------------------------------------------------
#--------------------------Brute Force Moves----------------------------
#-----------------------------------------------------------------------

listOfMoves = []

m0 = Move()
m0.x = 1
m0.y = 2
listOfMoves.append(m0)

m1 = Move()
m1.x = -1
m1.y = -2
listOfMoves.append(m1)

m2 = Move()
m2.x = 2
m2.y = -1
listOfMoves.append(m2)

m3 = Move()
m3.x = 1
m3.y = -2
listOfMoves.append(m3)

m4 = Move()
m4.x = 2
m4.y = 1
listOfMoves.append(m4)

m5 = Move()
m5.x = -2
m5.y = -1
listOfMoves.append(m5)

m6 = Move()
m6.x = -1
m6.y = 2
listOfMoves.append(m6)

m7 = Move()
m7.x = -2
m7.y = 1
listOfMoves.append(m7)

class Position: #Class for current position
#{
	def __init__(self):
	#{
		self.x = 0
		self.y = 0
	#}
#}

class Knight:   #Class for the "Character/piece"
#{
	def __init__(self):
	#{
		self.x = 0
		self.y = 0
	#}
	def moveEnding(self, move, numCol, numRow):
	#{
		tmpX = self.x
		tmpY = self.y
		tmpX += move.x
		tmpY += move.y
		return (tmpX >= 1 and tmpX <= numCol and tmpY>=1 and tmpY <= numRow)
	#}
	def move(self, move):
	#{
		self.x += move.x
		self.y += move.y
	#}
#}


#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

if (len(sys.argv) >= 4):
#{
	numRow = int(sys.argv[1])
	numCol = int(sys.argv[2])
	numTries = int(sys.argv[3])
#}
else:
#{
	numRow = 5
	numCol = 5
	numTries = 10000;
#}

listOfHoppedPositions = []
listOfTriedBoards = []



def wasVisited(knight, move):
#{
	newPos = Position()
	newPos.x = knight.x + move.x
	newPos.y = knight.y + move.y
	return contains(newPos, listOfHoppedPositions)
#}
#MY BRAIN, IT HURTS!

def contains(position, aList):
#{
  exists = False;
  for i in range(0,len(aList)):
  #{
     PositionCheck = aList[i]
     if(PositionCheck.x == position.x and PositionCheck.y == position.y):
     #{
        exists = True
        return exists
	 #}
  return exists
  #}
#}

def printBoard(listOfHoppedPositions):
#{
	#This will print the empty board
	board = []
	rows = ["x"] *numRow
	for i in range(0, numCol):#except for this one since it's one line
		board.append(list(rows))
	for i in range(1,len(listOfHoppedPositions)+1):
	#{
		pos = listOfHoppedPositions[i-1]
		board[pos.x-1][pos.y-1] = i
	#}
	output = ""
	for i in range(0, numRow):
	#{
		for k in range(0, numCol):
		#{
			#The board is being printed by k and i.
			output += str(board[k][i]) + " "
		#}
		output += '\n'
	#}
	return output
#}
def isSolved(listOfHoppedPositions):
#{
	complete = True
	for i in range(1, numCol+1):
	#{
		for k in range(1, numRow+1):
		#{
			newPos = Position()
			newPos.x = i
			newPos.y = k
			if(not contains(newPos, listOfHoppedPositions)):
			#{
				complete = False
				return complete
			#}
		#}
	#}
	return complete
#}
def getValidMoves(knight):
#{
	returnValue = []
	for i in range(0, len(listOfMoves)):
	#{
		move = listOfMoves[i]
		if(knight.moveEnding(move, numCol, numRow) and (not wasVisited(knight, move))): #This one also has 1 line
			returnValue.append(move)
	#}
	return returnValue
#}

#-----------------------------------------------------------------------
#--------------------------------Main-----------------------------------
#-----------------------------------------------------------------------
knight = Knight()
tries = 0;
itWorks = False;


while(itWorks == False and tries <= numTries):
#{
	tries +=1
	listOfTriedBoards.append(printBoard(listOfHoppedPositions))
	listOfHoppedPositions = []
	knight.x = 1;
	knight.y = 1;
	newPos = Position()
	newPos.x = knight.x
	newPos.y = knight.y
	listOfHoppedPositions.append(newPos)
	moved = True
	listOfValidMoves = getValidMoves(knight)
	while(len(listOfValidMoves) >0):
	#{
		listOfValidMoves = getValidMoves(knight)
		moved = False;
		r = random
		move = listOfValidMoves[r.randrange(0, len(listOfValidMoves))]
		knight.move(move)
		newPos = Position()
		newPos.x = knight.x
		newPos.y = knight.y
		listOfHoppedPositions.append(newPos)
		listOfValidMoves = getValidMoves(knight)
	#}
	if(isSolved(listOfHoppedPositions)):
		itWorks = True
#}

if(tries > numTries):
	print("Ugh, this wasn't supposed to happen, sorry Sergei or whoever is checking this." )
else:
	print("IT WORKED, IT WORKED! PARTY!")
print (printBoard(listOfHoppedPositions))


