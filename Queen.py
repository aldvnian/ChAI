import Bishop
from Rook import *
from Bishop import *
from Piece import *
from Board import *


class Queen(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)

    def display(self):
        return "Q"

    def getValidMoves(self):
        validMoves = [Bishop.getValidMoves(), Rook.getValidMoves()]
        return validMoves