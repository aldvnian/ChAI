from Player import *
from Piece import *
from pieceButton import *
import pygame

WRookImage = pygame.image.load('Images/WRook.png')
WRookImage = pygame.transform.scale(WRookImage, (700/8, 700/8))
WPawnImage = pygame.image.load('Images/WPawn.png')
WPawnImage = pygame.transform.scale(WPawnImage, (700/8, 700/8))
WBishopImage = pygame.image.load('Images/WBishop.png')
WBishopImage = pygame.transform.scale(WBishopImage, (700/8, 700/8))
WKingImage = pygame.image.load('Images/WKing.png')
WKingImage = pygame.transform.scale(WKingImage, (700/8, 700/8))
WKnightImage = pygame.image.load('Images/WKnight.png')
WKnightImage = pygame.transform.scale(WKnightImage, (700/8, 700/8))
WQueenImage = pygame.image.load('Images/WQueen.png')
WQueenImage = pygame.transform.scale(WQueenImage, (700/8, 700/8))
whitePieces = [WRookImage, WPawnImage, WBishopImage, WKingImage, WKnightImage, WQueenImage]

BRookImage = pygame.image.load('Images/BRook.png')
BRookImage = pygame.transform.scale(BRookImage, (700/8, 700/8))
BPawnImage = pygame.image.load('Images/BPawn.png')
BPawnImage = pygame.transform.scale(BPawnImage, (700/8, 700/8))
BBishopImage = pygame.image.load('Images/BBishop.png')
BBishopImage = pygame.transform.scale(BBishopImage, (700/8, 700/8))
BKingImage = pygame.image.load('Images/BKing.png')
BKingImage = pygame.transform.scale(BKingImage, (700/8, 700/8))
BKnightImage = pygame.image.load('Images/BKnight.png')
BKnightImage = pygame.transform.scale(BKnightImage, (700/8, 700/8))
BQueenImage = pygame.image.load('Images/BQueen.png')
BQueenImage = pygame.transform.scale(BQueenImage, (700/8, 700/8))
blackPieces = [BRookImage, BPawnImage, BBishopImage, BKingImage, BKnightImage, BQueenImage]

piecesLink = ['R', 'P', 'B', 'I', 'K', 'Q']


class Board:
    player1 = None
    player2 = None
    board = []
    for i in range(8):
        board.append([0] * 8)

    @staticmethod
    def __init__(player1: Player, player2: Player):
        Board.player1 = player1
        Board.player2 = player2

    @staticmethod
    def addPiece(x: int, y: int, piece: Piece):
        Board.board[y][x] = piece

    # Inputs:    INPUT DESCRIPTION
    #           Integer, Integer
    # Outputs:   Integer/Piece
    # Purpose:   Takes in a set of coordinates and returns 0 if no piece is at that location,
    #           or a reference to the Piece object otherwise
    @staticmethod
    def checkPiece(x: int, y: int) -> int | Piece:
        if x > 7 or x < 0 or y > 7 or y < 0:
            return -1
        return Board.board[y][x]

    # Outputs:   The boxes(_, |)
    # Purpose:   It creates the outline of the chess board and displays the pieces on the board

    @staticmethod
    def isPiece(row):
        storeOfPieces = []
        storeOfCoordinates = []
        for x in range(0, row):
            for y in range(0, len(Board.board[x])):
                if isinstance(Board.board[x][y], Piece):
                    piece = Board.board[x][y]
                    storeOfPieces.append(piece.display())
                    storeOfCoordinates.append((x, y))
        return storeOfPieces, storeOfCoordinates

    # Inputs:    Coordinates of the piece to be moved/coordinates of where to move them
    #           integer, integer, integer, integer
    # Outputs:   Final positions
    # Purpose:   To check the piece in the given coordinates and move them to the specified coordinates
    @staticmethod
    def movePiece(pieceX: int, pieceY: int, finalX: int, finalY: int):
        piece = Board.checkPiece(pieceX, pieceY)

        piece.setX(finalX)
        piece.setY(finalY)

        Board.board[finalY][finalX] = piece
        Board.board[pieceY][pieceX] = 0

    @staticmethod
    def testing():
        for row in Board.board:
            output = "|"
            for square in row:
                if square == 0:
                    output += "_"
                else:
                    output += square.display()
                output += "|"
            print(output)

    # Inputs:   pieces -> Piece[]
    # Purpose:  takes in a list of pieces and returns all possible squares that could be moved to
    #           by any of them
    # Outputs:  (integer, integer)[]
    @staticmethod
    def findPossibleMoves(pieces: list[Piece]) -> list[(int, int)]:
        listPieces = []
        for x in pieces:

            validMoves = x.getValidMoves()
            for move in validMoves:
                listPieces.append(move)

        setOfPossibleMoves = set(listPieces)
        return list(setOfPossibleMoves)
