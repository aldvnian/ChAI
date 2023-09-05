from Pawn import *
from Player import *


class Board:
    board = []

    for i in range(8):
        board.append([0] * 8)

    for x in range(8):
        board[0][x] = Pawn(1, x, 0, self)
        board[7][x] = Pawn(-1, x, 7, self)

    # Inputs:    INPUT DESCRIPTION
    #           Integer, Integer
    # Outputs:   Integer/Piece
    # Purpose:   Takes in a set of coordinates and returns 0 if no piece is at that location,
    #           or a reference to the Piece object otherwise
    @staticmethod
    def checkPiece(self, x, y):
        return Board.board[y][x]

    # Outputs:   The boxes(_, |)
    # Purpose:   It creates the outline of the chess board and displays the pieces on the board
    @staticmethod
    def display(self):
        for row in Board.board:
            output = "|"
            for square in row:
                if square == 0:
                    output += "_"
                else:
                    output += square.display()
                output += "|"
            print(output)

    # Inputs:    Coordinates of the piece to be moved/coordinates of where to move them
    #           integer, integer, integer, integer
    # Outputs:   Final positions
    # Purpose:   To check the piece in the given coordinates and move them to the specified coordinates
    @staticmethod
    def movePiece(self, Player.x, Player.y, Player.final_x, Player.final_y):

        piece = Board.checkPiece(pieceX, pieceY)
        if isinstance(piece, Pawn):
            piece.firstMove()

        piece.setX(finalX)
        piece.setY(finalY)

        Board.board[finalY][finalX] = piece
        Board.board[pieceY][pieceX] = 0





