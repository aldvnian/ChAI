from Piece import *

def Rook(Piece):
    def __init__(self, team, x, y, boardReference):
        super().__init__(team, x, y, boardReference)

    def move(self, x, y):
        if self[x][y] == self.getValidMoves:
            self.x = x
            self.y = y


