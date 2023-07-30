from Piece import *

class Pawn(Piece):
    def __init__(self, team, x, y, boardReference):
        super().__init__(team, x, y, boardReference)

    def Move(self):
        self.y = self.y + 1

    
