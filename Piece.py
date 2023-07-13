class Piece:
    def __init__(self, team, x, y):
        self.team = team
        self.x = x
        self.y = y
        
    def checkSameTeam(self, otherPiece):
        return self.team == otherPiece.team
        
    def getX(self):
        return self.x
        
    def setX(self):
        self.x = x
        
    def getY(self):
        return self.y
        
    def setY(self):
        self.y = y
        
    def getValidMoves(self, board):
        pass
