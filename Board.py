class Board:
    player1 = None
    player2 = None
    board = []

    @staticmethod
    def __init__(player1, player2):
        Board.player1 = player1
        Board.player2 = player2

    @staticmethod
    def addPiece(x, y, piece):
        Board.board[y][x] = piece

    # Inputs:    INPUT DESCRIPTION
    #           Integer, Integer
    # Outputs:   Integer/Piece
    # Purpose:   Takes in a set of coordinates and returns 0 if no piece is at that location,
    #           or a reference to the Piece object otherwise
    @staticmethod
    def checkPiece(x, y):
        if x > 7 or x < 0 or y > 7 or y < 0:
            return -1
        return Board.board[y][x]

    # Outputs:   The boxes(_, |)
    # Purpose:   It creates the outline of the chess board and displays the pieces on the board
    @staticmethod
    def __repr__(self):
        for row in Board.board:
            output = "|"
            for square in row:
                if square == 0:
                    output += "_"
                else:
                    output += square.display()
                output += "|"
            print(output)

    # Inputs:    Coordinates of the piece to be moved/coordinates of where to move them
    #           integer, integer, integer, integer
    # Outputs:   Final positions
    # Purpose:   To check the piece in the given coordinates and move them to the specified coordinates
    @staticmethod
    def movePiece(pieceX, pieceY, finalX, finalY):
        piece = Board.checkPiece(pieceX, pieceY)

        piece.setX(finalX)
        piece.setY(finalY)

        Board.board[finalY][finalX] = piece
        Board.board[pieceY][pieceX] = 0