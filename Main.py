from Player import *
#Imports from Board class
from Board import *

player1 = Player("player1",1 )
player2 = Player("player2", -1)

Game.__init__(player1, player2)

while True:
    Game.doTurn()
