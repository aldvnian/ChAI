from Piece import *


class Rook(Piece):
    def __init__(self, x, y, boardReference):
        super().__init__(x, y, boardReference)

    def display(self):
        print("R")
