class Piece:##I     Inputs:   - team -> integer
     #           - x -> integer
     #           - y -> integer
     # Process:  Assigns variables when object is contructed def __init__(self, team, x, y):
        self.team = team
        self.x = x
        self.y = y

#Method fo    r checking if a piece is in your team or opponent's
#Input: oth    erPiece
    def checkSameTeam(self, otherPiece):
        return self.team == otherPiece.team
#Gets the x 
c        o    ordinate of a piece
    def getX(self):
        return self.x
#Sets the x coo
r        d    inate of a piece
    def setX(self, x):
        self.x = x
#Gets the y coordi
n        a    te of a piece
    def getY(self):
        return self.y
#Sets the y coordinat
e             of a piece
    def setY(self, y):
        self.y = y
#Method for getting the 
s        e    t of valid moves for a given piece
#Input: board
    def getVa    lidMoves(self):
        pass
#Method for displaying a pie
c    e    
    def display(self):
        pass
