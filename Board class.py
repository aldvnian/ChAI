class Board:
    def __init__(self):
        self.board = []
        for i in range(8):
            self.board.append([0] * 8)
        print(self.board)

theBoard = Board()
