from Pawn import *


class Board:
    def __init__(self):
        self.board = []

        for i in range(8):
            self.board.append([0] * 8)

        for x in range(8):
            self.board[0][x] = Pawn(0, x, 0, self)
            self.board[7][x] = Pawn(1, x, 7, self)

    def checkPiece(self, x, y):
        return self.board[y][x]

    def display(self):
        for row in self.board:
            output = "|"
            for square in row:
                if square == 0:
                    output += "_"
                else:
                    output += square.display()
                output += "|"
            print(output)
