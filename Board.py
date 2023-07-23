class Board:
    def __init__(self, team):
        self.team = team
        self.board = []
        for i in range(8):
            self.board.append([0] * 8)
        print(self.board)
        for x in range(8):
            self.board[0][x] = Piece()
            self.board[7][x] = Piece()
theBoard = Board()
