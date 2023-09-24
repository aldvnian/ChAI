from Piece import *

class King(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)

    def display(self):
        return "K"

    def getValidMoves(self):
        if Board.checkpiece(self.getX, self.getY + team) == 0:
            
