from Player import *
from Game import *
from UI import *
from Button import *
import pygame

pygame.init()

player1 = Player("player1", 1)
player2 = Player("player2", -1)

Game.__init__(player1, player2)

width, height = 1000, 700
screen = pygame.display.set_mode([width, height])

run = True
fps = 60
timer = pygame.time.Clock()
phase = 0

while run:
    timer.tick(fps)
    mouse = pygame.mouse.get_pos()
    mainMenu(screen)

        # if screenName == 'play':
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         xCoordinate, yCoordinate = event.pos[0] // (700/8), event.pos[1] // (700/8)
        #         print(xCoordinate, yCoordinate)
        #         pieceAtPos = Board.checkPiece(xCoordinate, yCoordinate)
        #         if isinstance(pieceAtPos, Piece):
        #             if Game.currentPlayer.isPlayerPiece(pieceAtPos):
        #                 selection = pieceAtPos
        #                 Game.pieceX, Game.pieceY = xCoordinate, yCoordinate
        #         xMove, yMove = event.pos[0], event.pos[1]
        #         if (xMove, yMove) in selection.getValidMoves():
        #             Game.moveX, Game.moveY = xMove, yMove
        #             Game.move()
