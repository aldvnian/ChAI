from Piece import *

class Player(Piece):
  def __init__(self, name):
    self.name = name
    self.x = int(input("Enter the X-Coordinate of the piece you want to move"))
    self.y = int(input("Enter the Y-Coordinate of the piece you want to move"))
    self.final_x = int(input("Enter the X-Coordinate of where you want to move it"))
    self.final_y = int(input("Enter the Y-Coordinate of where you want to move it"))
