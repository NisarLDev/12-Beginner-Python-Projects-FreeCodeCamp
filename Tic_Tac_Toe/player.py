import math
import random

class Player:
    def __init__(self, letter):
      # letter is x or o
      self.letter = letter
  
    # we want all players to get their next move a game
    def get_move(self, game):
      pass
   
class RandomComputerPlayer(Player):
    def __init__(self, letter):
