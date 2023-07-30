from Piece import *

class Pawn(Piece):
    def __init__(self, team, x, y, boardReference):
        super().__init__(team, x, y, boardReference)
        self.hasMoved = False

    def getValidMoves(self):
        validMoves = []
        
        if self.board.checkPiece(self.getX(), self.getY() + team) == 0:
            validMoves.append((self.getX(), self.getY() + team)
            if not self.hasMoved and self.board.checkPiece(self.getX(), self.getY() + (2 * team)) == 0:
                validMoves.append((self.getX(), self.getY() + (2 * team)))

        if self.board.checkPiece(self.getX() + 1, self.getY() + team) == 0:
            validMoves.append((self.getX() + 1, self.getY() + team))
            
        if self.board.checkPiece(self.getX() - 1, self.getY() + team) == 0:
            validMoves.append((self.getX() - 1, self.getY() + team))
    
        
        return validMoves

    def display(self):
        return "P"
        
    def firstMove(self):
        self.hasMoved = True
