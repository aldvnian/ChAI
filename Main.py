from Player import *
from Game import *
from AI import *

player1 = Player("player1", 1)
player2 = Player("player2", -1)
engine = AI(player2, player1)

Game.__init__(player1, engine)

while not Game.isCheckmate:
    Game.doTurn()
print("Game over!")
