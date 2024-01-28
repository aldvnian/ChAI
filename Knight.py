from Piece import *
from Board import *
class Knight(Piece):
    def display(self):
        return 'K'

    def getValidMoves(self):
        validMoves = []
        x, y = self.getX(), self.getY()

        if x - 2 < 0 or y + 1 > 7:
            pass
        else:
            currentSquare = Board.checkPiece(x - 2, y + 1)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    validMoves.append((x - 2, y + 1))

        x, y = self.getX(), self.getY()

        if x - 2 < 0 or y - 1 < 0:
            pass
        else:
            currentSquare = Board.checkPiece(x - 2, y - 1)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    validMoves.append((x - 2, y - 1))

        x, y = self.getX(), self.getY()

        if x + 2 > 7 or y + 1 > 7:
            pass
        else:
            currentSquare = Board.checkPiece(x + 2, y + 1)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    validMoves.append((x + 2, y + 1))

        x, y = self.getX(), self.getY()

        if x + 2 > 7 or y - 1 < 0:
            pass
        else:
            currentSquare = Board.checkPiece(x + 2, y - 1)
            if currentSquare != 0:
                if not self.checkSameTeam(currentSquare):
                    validMoves.append((x + 2, y - 1))
