from Piece import *
class Rook(Piece):
    def __init__(self):
        super().__init__(team, x, y)
    
    def display(self):
        return "R" 
    
    def getValidMoves(self):
        pass
