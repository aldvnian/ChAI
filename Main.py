from Board import *
board = Board()
runGame = True
playerTurn = 1

while runGame:
    board.display()
    validMove = False
    
    while not validMove:
        pieceX = int(input("Enter your pieces x co-ordinate"))
        pieceY = int(input("Enter your pieces y co-ordinate"))
        moveX = int(input("Enter the x co-ordinate you wish to move to"))
        moveY = int(input("Enter the y co-ordinate you wish to move to"))
        theSquare = board.checkPiece(pieceX, pieceY)
        if (moveX, moveY) in theSquare.getValidMoves():
        #move is valid
            board.movePiece(pieceX, pieceY, moveX, moveY)
            validMove = True
        else:
            print("Invalid move for that piece!")
        if playerTurn == 1:
            playerTurn = -1
        else:
            playerTurn = 1
