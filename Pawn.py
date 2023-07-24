from Piece import *

class Pawn(Piece):
  def __init__(self, team, x, y, boardRef):
    super().__init__(team, x, y, boardRef)

  def Move(self):
    self.y = self.y + 1

  def Kill_left(self):
    self.y = self.y + 1
    self.x = self.x - 1

  def Kill_right(self):
    self.y = self.y + 1
    self.x = self.x + 1

    
