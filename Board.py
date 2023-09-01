
from Pawn import *

class Board:
    
    @staticmethod
    # Process:  ADD DESCRIPTION
    def __init__(self):
        self.board = []

        for i in range(8):
            self.board.append([0] * 8)

        for x in range(8):
            self.board[0][x] = Pawn(1, x, 0, self)
            self.board[7][x] = Pawn(-1, x, 7, self)

    #Inputs:    INPUT DESCRIPTION
    #           Integer, Integer
    #Outputs:   Integer/Piece
    #Purpose:   Takes in a set of coordinates and returns 0 if no piece is at that location, 
    #           or a reference to the Piece object otherwise
    @staticmethod
    def checkPiece(self, x, y):
        return self.board[y][x]

    #Outputs:   The boxes(_, |)
    #Purpose:   It creates the outline of the chess board and displays the pieces on the board
    @staticmethod
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

    #Inputs:    Coordinates of the piece to be moved/coordinates of where to move them 
    #           integer, integer, integer, integer
    #Outputs:   Final positions
    #Purpose:   To check the piece in the given coordinates and move them to the specified coordinates
    @staticmethod
    def movePiece(self, pieceX, pieceY, finalX, finalY):

        piece = self.checkPiece(pieceX, pieceY)
        if isinstance(piece, Pawn):
            piece.firstMove()

        piece.setX(finalX)
        piece.setY(finalY)

        self.board[finalY][finalX] = piece
        self.board[pieceY][pieceX] = 0






