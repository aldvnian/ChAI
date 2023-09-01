from Piece import *

#Input: team 1,-1 - x, y, boardReference
#initialising the constructor and setting a variable to record whether a pawn has moved
class Pawn(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)
        self.hasMoved = False
#Output: all the valid moves for pawns
#Stores valid moves for pawns
    def getValidMoves(self):
        validMoves = []
        
        if Board.checkPiece(self.getX(), self.getY() + self.team) == 0:
            validMoves.append((self.getX(), self.getY() + self.team))
            if not self.hasMoved and Board.checkPiece(self.getX(), self.getY() + (2 * self.team)) == 0:
                validMoves.append((self.getX(), self.getY() + (2 * self.team)))

        if Board.checkPiece(self.getX() + 1, self.getY() + self.team) == 0:
            validMoves.append((self.getX() + 1, self.getY() + self.team))
            
        if Board.checkPiece(self.getX() - 1, self.getY() + self.team) == 0:
            validMoves.append((self.getX() - 1, self.getY() + self.team))
    
        
        return validMoves
#Output: displays "P" for pawn
    def display(self):
        return "P"
#Sets pawns to have moved
    def firstMove(self):
        self.hasMoved = True
