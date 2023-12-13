from Player import *
from Rook import *
from Bishop import *
from Board import *

class Queen(Piece):
    def __init__(self, team, x, y):
        super.__init__(team, x, y)
    
    def getValidMoves(self):
        ValidMoves = []
        

    def display(self):
        return 'Q'
