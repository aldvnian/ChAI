from Piece import *
from Board import *


class Knight(Piece):
    def display(self):
        return 'K'

    #Method for producing all the valid moves that are two squares to the left and one square up from the knight
    def TwoLeftUp(self):
        x, y = self.getX(), self.getY()
        if (x - 2 >= 0) and (y + 1 <= 7):
            currentSquare = Board.checkPiece(x - 2, y + 1)
            if isinstance(currentSquare, Piece):
                if not self.checkSameTeam(currentSquare):
                    return x - 2, y + 1
            else:
                return x - 2, y + 1

    #Method for producing all the valid moves that are two squares to the left and one square down from the knight
    def TwoLeftDown(self):
        x, y = self.getX(), self.getY()
        if (x - 2 >= 0) and (y - 1 >= 0):
            currentSquare = Board.checkPiece(x - 2, y - 1)
            if isinstance(currentSquare, Piece):
                if not self.checkSameTeam(currentSquare):
                    return x - 2, y - 1
            else:
                return x - 2, y - 1

    #Method for producing all the valid moves that are two squares to the right and one square up from the knight
    def TwoRightUp(self):
        x, y = self.getX(), self.getY()
        if (x + 2 <= 7) and (y + 1 <= 7):
            currentSquare = Board.checkPiece(x + 2, y + 1)
            if isinstance(currentSquare, Piece):
                if not self.checkSameTeam(currentSquare):
                    return x + 2, y + 1
            else:
                return x + 2, y + 1

    #Method for producing all the valid moves that are two squares to the right and one square down from the knight
    def TwoRightDown(self):
        x, y = self.getX(), self.getY()
        if (x + 2 <= 7) and (y - 1 >= 0):
            currentSquare = Board.checkPiece(x + 2, y - 1)
            if isinstance(currentSquare, Piece):
                if not self.checkSameTeam(currentSquare):
                    return x + 2, y - 1
            else:
                return x + 2, y - 1

    #Method for producing all the valid moves that are one square left and two squares up from the knight
    def OneLeftUp(self):
        x, y = self.getX(), self.getY()
        if (y + 2 <= 7) and (x - 1 >= 0):
            currentSquare = Board.checkPiece(x - 1, y + 2)
            if isinstance(currentSquare, Piece):
                if not self.checkSameTeam(currentSquare):
                    return x - 1, y + 2
            else:
                return x - 1, y + 2

    #Method for producing all the valid moves that are one square left and two squares down from the knight
    def OneLeftDown(self):
        x, y = self.getX(), self.getY()
        if (y - 2 >= 0) and (x - 1 >= 0):
            currentSquare = Board.checkPiece(x - 1, y - 2)
            if isinstance(currentSquare, Piece):
                if not self.checkSameTeam(currentSquare):
                    return x - 1, y - 2
            else:
                return x - 1, y - 2

    #Method for producing all the valid moves that are one square right and two squares up from the knight
    def OneRightUp(self):
        x, y = self.getX(), self.getY()
        if (y + 2 <= 7) and (x + 1 <= 7):
            currentSquare = Board.checkPiece(x + 1, y + 2)
            if isinstance(currentSquare, Piece):
                if not self.checkSameTeam(currentSquare):
                    return x + 1, y + 2
            else:
                return x + 1, y + 2

    #Method for producing all the valid moves that are one square right and two squares down from the knight
    def OneRightDown(self):
        x, y = self.getX(), self.getY()
        if (y - 2 >= 0) and (x + 1 <= 7):
            currentSquare = Board.checkPiece(x + 1, y - 2)
            if isinstance(currentSquare, Piece):
                if not self.checkSameTeam(currentSquare):
                    return x + 1, y - 2
            else:
                return x + 1, y - 2

    #Method for retrieving all of the valid moves for the knight
    def getValidMoves(self):
        validMoves = [self.TwoLeftUp(), self.TwoLeftDown(), self.TwoRightUp(), self.TwoRightDown(), self.OneLeftUp(),
                      self.OneLeftDown(), self.OneRightUp(), self.OneRightDown()]

        return [valid for valid in validMoves if valid is not None]
