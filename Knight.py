from Piece import *
from Board import *


class Knight(Piece):
    def display(self):
        return 'K'

    def TwoLeftUp(self):
        x, y = self.getX(), self.getY()
<<<<<<< HEAD
        if (x - 2 >= 0) and (y + 1 <= 7):
            currentSquare = Board.checkPiece(x - 2, y + 1)
            if isinstance(currentSquare, Piece):
=======
        if (x - 2 >= 0) or (y + 1 <= 7):
            currentSquare = Board.checkPiece(x - 2, y + 1)
            if currentSquare != 0:
>>>>>>> origin/GameLogic
                if not self.checkSameTeam(currentSquare):
                    return x - 2, y + 1
            else:
                return x - 2, y + 1

    def TwoLeftDown(self):
        x, y = self.getX(), self.getY()
<<<<<<< HEAD
        if (x - 2 >= 0) and (y - 1 >= 0):
            currentSquare = Board.checkPiece(x - 2, y - 1)
            if isinstance(currentSquare, Piece):
=======
        if (x - 2 >= 0) or (y - 1 >= 0):
            currentSquare = Board.checkPiece(x - 2, y - 1)
            if currentSquare != 0:
>>>>>>> origin/GameLogic
                if not self.checkSameTeam(currentSquare):
                    return x - 2, y - 1
            else:
                return x - 2, y - 1

    def TwoRightUp(self):
        x, y = self.getX(), self.getY()
<<<<<<< HEAD
        if (x + 2 <= 7) and (y + 1 <= 7):
            currentSquare = Board.checkPiece(x + 2, y + 1)
            if isinstance(currentSquare, Piece):
=======
        if (x + 2 <= 7) or (y + 1 <= 7):
            currentSquare = Board.checkPiece(x + 2, y + 1)
            if currentSquare != 0:
>>>>>>> origin/GameLogic
                if not self.checkSameTeam(currentSquare):
                    return x + 2, y + 1
            else:
                return x + 2, y + 1

    def TwoRightDown(self):
        x, y = self.getX(), self.getY()
<<<<<<< HEAD
        if (x + 2 <= 7) and (y - 1 >= 0):
            currentSquare = Board.checkPiece(x + 2, y - 1)
            if isinstance(currentSquare, Piece):
=======
        if (x + 2 <= 7) or (y - 1 >= 0):
            currentSquare = Board.checkPiece(x + 2, y - 1)
            if currentSquare != 0:
>>>>>>> origin/GameLogic
                if not self.checkSameTeam(currentSquare):
                    return x + 2, y - 1
            else:
                return x + 2, y - 1

    def OneLeftUp(self):
        x, y = self.getX(), self.getY()
<<<<<<< HEAD
        if (y + 2 <= 7) and (x - 1 >= 0):
            currentSquare = Board.checkPiece(x - 1, y + 2)
            if isinstance(currentSquare, Piece):
=======
        if (y + 2 <= 7) or (x - 1 >= 0):
            currentSquare = Board.checkPiece(x - 1, y + 2)
            if currentSquare != 0:
>>>>>>> origin/GameLogic
                if not self.checkSameTeam(currentSquare):
                    return x - 1, y + 2
            else:
                return x - 1, y + 2

    def OneLeftDown(self):
        x, y = self.getX(), self.getY()
<<<<<<< HEAD
        if (y - 2 >= 0) and (x - 1 >= 0):
            currentSquare = Board.checkPiece(x - 1, y - 2)
            if isinstance(currentSquare, Piece):
=======
        if (y - 2 >= 0) or (x - 1 >= 0):
            currentSquare = Board.checkPiece(x - 1, y - 2)
            if currentSquare != 0:
>>>>>>> origin/GameLogic
                if not self.checkSameTeam(currentSquare):
                    return x - 1, y - 2
            else:
                return x - 1, y - 2

    def OneRightUp(self):
        x, y = self.getX(), self.getY()
<<<<<<< HEAD
        if (y + 2 <= 7) and (x + 1 <= 7):
            currentSquare = Board.checkPiece(x + 1, y + 2)
            if isinstance(currentSquare, Piece):
=======
        if (y + 2 <= 7) or (x + 1 <= 7):
            currentSquare = Board.checkPiece(x + 1, y + 2)
            if currentSquare != 0:
>>>>>>> origin/GameLogic
                if not self.checkSameTeam(currentSquare):
                    return x + 1, y + 2
            else:
                return x + 1, y + 2

    def OneRightDown(self):
        x, y = self.getX(), self.getY()
<<<<<<< HEAD
        if (y - 2 >= 0) and (x + 1 <= 7):
            currentSquare = Board.checkPiece(x + 1, y - 2)
            if isinstance(currentSquare, Piece):
=======
        if (y - 2 >= 0) or (x + 1 <= 7):
            currentSquare = Board.checkPiece(x + 1, y - 2)
            if currentSquare != 0:
>>>>>>> origin/GameLogic
                if not self.checkSameTeam(currentSquare):
                    return x + 1, y - 2
            else:
                return x + 1, y - 2

    def getValidMoves(self):
        validMoves = [self.TwoLeftUp(), self.TwoLeftDown(), self.TwoRightUp(), self.TwoRightDown(), self.OneLeftUp(),
                      self.OneLeftDown(), self.OneRightUp(), self.OneRightDown()]

<<<<<<< HEAD
=======
        print(validMoves)
>>>>>>> origin/GameLogic
        return validMoves
