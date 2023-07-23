class Pawn(Pieces):
  def __init__(self):
    super.()__init__(team, x, y):

  def Move(self):
    self.y = self.y + 1

  def Kill_left(self):
    self.y = self.y + 1
    self.x = self.x - 1

  def Kill_right(self):
    self.y = self.y + 1
    self.x = self.x + 1

  def Promote(self):
    
