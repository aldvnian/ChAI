

class Player:
    def __init__(self, name, direction):
        self.name = name
        self.direction = direction
        self.pieces = []

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
