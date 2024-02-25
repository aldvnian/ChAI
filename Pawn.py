from Piece import *
from Board import *

#Input: team 1,-1 - x, y, boardReference
#initialising the constructor and setting a variable to record whether a pawn has moved
class Pawn(Piece):
    def __init__(self, team, x, y):
        super().__init__(team, x, y)
        self.hasMoved = False

    #Output: all the valid moves for pawns
    #Stores valid moves for pawn
    def getValidMoves(self):
        validMoves = []
        
        if Board.checkPiece(self.getX(), self.getY() + self.team) == 0:
            validMoves.append((self.getX(), self.getY() + self.team))
            if not self.hasMoved and Board.checkPiece(self.getX(), self.getY() + (2 * self.team)) == 0:
                validMoves.append((self.getX(), self.getY() + (2 * self.team)))

        if not isinstance(Board.checkPiece(self.getX() + 1, self.getY() + self.team), int):
            pieceAtSquare = Board.checkPiece(self.getX() + 1, self.getY() + self.team)
            if not pieceAtSquare.checkSameTeam(self):
                validMoves.append((self.getX() + 1, self.getY() + self.team))
            
        if not isinstance(Board.checkPiece(self.getX() - 1, self.getY() + self.team), int):
            pieceAtSquare = Board.checkPiece(self.getX() - 1, self.getY() + self.team)
            if not pieceAtSquare.checkSameTeam(self):
                validMoves.append((self.getX() - 1, self.getY() + self.team))
    
        
        return [valid for valid in validMoves if valid is not None]
        
    #Output: displays "P" for pawn
    def display(self):
        return "P"

    #Sets pawns to have moved
    def firstMove(self):
        self.hasMoved = True

    def setY(self, y):
        super().setY(y)
        self.firstMove()
