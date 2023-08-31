#Imports from Board class
from Board import *
board = Board()
runGame = True
playerTurn = 1

while runGame:
    board.display()
    validMove = False
#Sets out the game to ask for inputs while validMove is True
#Input: Coordinates of the piece to be moved and the coordinates where the piece is to be moved/Integer
    while not validMove:
        pieceX = int(input("Enter your pieces x co-ordinate"))
        pieceY = int(input("Enter your pieces y co-ordinate"))

        moveX = int(input("Enter the x co-ordinate you wish to move to"))
        moveY = int(input("Enter the y co-ordinate you wish to move to"))
#Redundant?
#Output: print statements/Characters
        theSquare = board.checkPiece(pieceX, pieceY)
        if theSquare != 0:
            if (moveX, moveY) in theSquare.getValidMoves():
                #move is valid
                board.movePiece(pieceX, pieceY, moveX, moveY)
                validMove = True
            else:
                print("Invalid move for that piece!")
        else:
            print("No piece at that location!")
#Swaps player turns
        if playerTurn == 1:
            playerTurn = -1
        else:
            playerTurn = 1
