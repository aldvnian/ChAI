from Player import *
from Rook import *
from Board import *

class Queen(Piece):
    def __init__(self, team, x, y):
        super.__init__(team, x, y)

    def maxX(self):
        for x in range(self.x, 7)
    
    def getValidMoves(self):
        ValidMoves = []
        

    def display(self):
        return 'Q'
