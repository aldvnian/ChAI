class Piece:
#Initialising the constructor
#Input: team, x, y, boardReference
    def __init__(self, team, x, y):
        self.team = team
        self.x = x
        self.y = y

#Method for checking if a piece is in your team or opponent's
#Input: otherPiece
    def checkSameTeam(self, otherPiece):
        return self.team == otherPiece.team
#Gets the x coordinate of a piece
    def getX(self):
        return self.x
#Sets the x coordinate of a piece
    def setX(self, x):
        self.x = x
#Gets the y coordinate of a piece
    def getY(self):
        return self.y
#Sets the y coordinate of a piece
    def setY(self, y):
        self.y = y
#Method for getting the set of valid moves for a given piece
#Input: board
    def getValidMoves(self):
        pass
#Method for displaying a piece
    def display(self):
        pass
