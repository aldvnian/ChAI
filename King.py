from Piece import *

class King:
    def __init__(self):
        super().__init__(team, x, y)

    def display(self):
        return "K"

    def get_validmoves():
        if Board.checkpiece(self.getX, self.getY + team) == 0:
            
