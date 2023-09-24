#Imports from Board class
from Board import *

runGame = True
playerTurn = 1

while runGame:
    print(Board)
    validMove = False
    #Sets out the game to ask for inputs while validMove is True
    
    while not validMove:
        # pieceX and pieceY are the pieces current coordinates
        pieceX = int(input("Enter your pieces x co-ordinate"))
        pieceY = int(input("Enter your pieces y co-ordinate"))

        # pieceX and pieceY are the pieces destination coordinates
        moveX = int(input("Enter the x co-ordinate you wish to move to"))
        moveY = int(input("Enter the y co-ordinate you wish to move to"))
        
        theSquare = Board.checkPiece(pieceX, pieceY)
        if theSquare != 0:
            if (moveX, moveY) in theSquare.getValidMoves():
                #move is valid
                validMove = True                
                Board.movePiece(pieceX, pieceY, moveX, moveY)
            else:
                print("Invalid move for that piece!")
        else:
            print("No piece at that location!")

        #Swaps player turns
        if playerTurn == 1:
            playerTurn = -1
        else:
            playerTurn = 1

