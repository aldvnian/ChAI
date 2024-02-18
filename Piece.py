

class Piece:
    #Inputs:    - team -> integer
    #           - x -> integer
    #           - y -> integer
    #Process:   - Assigns variables when a Piece object is constructed
    def __init__(self, team, x, y):
        self.team = team
        self.team_flag = self.team.name + "_flag"
        self.x = x
        self.y = y
        self.team.addPiece(self) #team is assigned with a player instance so the addPiece function adds
#the piece into player

    #Method for checking if a piece is in your team or opponent's
    #Input: otherPiece
    def checkSameTeam(self, otherPiece):
        return self.team == otherPiece.team

    #Gets the x coordinate of a piece
    def getX(self):
        return self.x

    # Input: Integer
    # Process: Sets the x coordinate of a piece
    def setX(self, x):
        self.x = x

    #Process: Gets the y coordinate of a piece
    #Output: Integer
    def getY(self):
        return self.y
        
    #Sets the y coordinate of a piece
    def setY(self, y):
        self.y = y

    def getTeam(self):
        return self.team

    #Process: Method for getting the set of valid moves for a given piece
    def getValidMoves(self):
        pass
    
    #Method for displaying a piece
    def display(self):
        pass
    

