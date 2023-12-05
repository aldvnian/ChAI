from Player import *
from Rook import *
from Board import *

class Queen(Piece):
    def __init__(self, x, y):
        super.__init__(x, y)
        self.player = Player()

    
    def getValidMoves(self):
        ValidMoves = []

    def display(self):
        return 'Q'
