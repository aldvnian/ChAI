from colorama import Fore, Style
from Player import *
from Piece import *
import pygame

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
        print(f'IM HERE: {x},{y}')
        if x > 7 or x < 0 or y > 7 or y < 0:
            print(f'Invalid move: {x},{y}')
            return -1
        return Board.board[y][x]

    # Outputs:   The boxes(_, |)
    # Purpose:   It creates the outline of the chess board and displays the pieces on the board
    @staticmethod
    def displayBoard():
        for row in Board.board:
            output = "|"
            for square in row:
                if square == 0:
                    output += "_"
                else:
                    pieceToAdd = square.display()
                    # TODO: change it so rather than colour being hardcoded it is fetched from the player object
                    if square.team == Board.player1:
                        pieceToAdd = Fore.RED + pieceToAdd
                    else:
                        pieceToAdd = Fore.BLUE + pieceToAdd

                    output += pieceToAdd + Style.RESET_ALL
                output += "|"
            print(output)

    # Inputs:    Coordinates of the piece to be moved/coordinates of where to move them
    #           integer, integer, integer, integer
    # Outputs:   Final positions
    # Purpose:   To check the piece in the given coordinates and move them to the specified coordinates
    @staticmethod
    def movePiece(pieceX: int, pieceY: int, finalX: int, finalY: int):
        piece = Board.checkPiece(pieceX, pieceY)

        if type(piece) is int and piece <= 0:
            return
        piece.setX(finalX)
        piece.setY(finalY)

        Board.board[finalY][finalX] = piece
        Board.board[pieceY][pieceX] = 0

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