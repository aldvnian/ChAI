from Player import *
from Rook import *

class Queen(Piece):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.player = Player()

    def getValidMoves():
        ValidMoves = []
