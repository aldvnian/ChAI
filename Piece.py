class Piece:

    def __init__(self, team, x, y, boardReference):
        self.team = team
        self.x = x
        self.y = y
        self.board = boardReference

    def checkSameTeam(self, otherPiece):
        return self.team == otherPiece.team

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getValidMoves(self, board):
        pass

    def display(self):
        pass
