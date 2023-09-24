from Piece import *
from Board import *

class King(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)

    def display(self):
        return "K"

    def getValidMoves(self):
        validMoves = []
        x, y = self.getX, self.getY

        topLeft = Board.checkPiece(x + 1, y + 1)
        if topLeft == 0:
            validMoves.append((x + 1, y + 1))
        elif isinstance(topLeft, Piece):
            if not self.checkSameTeam(topLeft):
                validMoves.append((x + 1, y + 1))