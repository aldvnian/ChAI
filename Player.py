

class Player:
    def __init__(self, name, direction):
        self.name = name
        self.direction = direction
        self.pieces = []
        self.king = 0

    def addPiece(self, piece):
        self.pieces.append(piece)

    def isPlayerPiece(self, piece):
        return piece in self.pieces

    def __add__(self, value):
        return value + self.direction

    def __radd__(self, value):
        return value + self.direction

    def __mul__(self, value):
        return value * self.direction

    def __rmul__(self, value):
        return value * self.direction

    def removePiece(self, piece):
        self.pieces.remove(piece)

    def getPieces(self):
        return self.pieces

    def getKingCoordinates(self):
        return self.king.getX(), self.king.getY()