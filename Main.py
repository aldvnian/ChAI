from Board import *

board = Board()

runGame = True

playerTurn = 1

while runGame:
    board.display()

    pieceX = int(input("Enter your pieces x co-ordinate"))
    pieceY = int(input("Enter your pieces y co-ordinate"))

    moveX = int(input("Enter the x co-ordinate you wish to move to"))
    moveY = int(input("Enter the y co-ordinate you wish to move to"))

    board.movePiece(pieceX, pieceY, moveX, moveY)

    if playerTurn == 1:
        playerTurn = -1
    else:
        playerTurn = 1