import sys
import copy
import os #allows you to execute code from CMD
from time import sleep

#python C:\Users\Danii\Desktop\COSC1352\gameoflife.py < "C:\Users\Danii\Desktop\COSC1352\seed10.txt"


def printBoard(board):
    print " ",
    for col in range (0,len(board)):
        print (col % 10),
    print   
    for row in range(0,len(board)):
        print (row % 10),
        for col in range(len(board)):
            print board[row][col],
        print

def computeNextGen(board):
    nextBoard = copy.deepcopy(board) #need to create a new data structure not with same memory location This is known is a deep copyright
    for row in range (1, len(board)-1):
        for col in range (1, len(board)-1):
            neighbors = countNeighbors(board, row, col)
            if(board[row][col] == "*"):
                if (neighbors < 2 or neighbors > 3):
                    nextBoard[row][col] = " "
            else:
                if(neighbors == 3):
                    nextBoard[row][col] = "*"
    return nextBoard


def countNeighbors(board, row, col):
    neighbors = 0
    for i in range (-1,2):
        for j in range(-1,2):
            if(not (i == 0 and j ==0)):
                if(board[row + i] [col + j] == "*"):
                        neighbors += 1
    return neighbors


board = []
for line in sys.stdin:
  board.append([])
  for c in range(len(line)-1):
    board[len(board)-1].append(line[c])


print "Generation 0"
NUM_GENS = 10

printBoard(board)
os.system("cls")


for gen in range(NUM_GENS):
        sleep(0.9)
        os.system("cls")
        print "Generation", (gen + 1)
        board = computeNextGen(board)
        #if (board == nextBoard):
        printBoard(board)
