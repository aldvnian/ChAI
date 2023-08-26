from Pawn import *

# Initialising Board class
class Board:
    def __init__(self):
        self.board = []

        for i in range(8):
            self.board.append([0] * 8)

        for x in range(8):
            self.board[0][x] = Pawn(1, x, 0, self)
            self.board[7][x] = Pawn(-1, x, 7, self)

#Inputs: Integer/Integer
#Outputs: Integer/Piece
#Purpose: It observes a specific coordinate in the board and returns what is
#in that coordinate
    def checkPiece(self, x, y):
        return self.board[y][x]

#Inputs:
#Outputs: The boxes(_, |)
#Purpose: It creates the outline of the chess board and displays the pieces on the board
    def display(self):
        for row in self.board:
            output = "|"
            for square in row:
                if square == 0:
                    output += "_"
                else:
                    output += square.display()
                output += "|"
            print(output)

#Inputs: Coordinates of the piece to be moved/coordinates of where to move them
#Outputs: Final positions
#Purpose: To check the piece in the given coordinates and move them to the specified coordinates
    def movePiece(self, pieceX, pieceY, finalX, finalY):

        piece = self.checkPiece(pieceX, pieceY)
        if isinstance(piece, Pawn):
            piece.firstMove()

        piece.setX(finalX)
        piece.setY(finalY)

        self.board[finalY][finalX] = piece
        self.board[pieceY][pieceX] = 0
