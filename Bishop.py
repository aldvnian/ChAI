from Board import *
from Piece import *
def Bishop(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)

    def display(self):
        return "B"

    def topLeft(self):
        pass

    def topRight(self):
        pass

    def bottomLeft(self):
        pass

    def bottomRight(self):
        pass


    def getValidMoves(self):
        x, y = self.getX(), self.getY()
        validMoves = []
