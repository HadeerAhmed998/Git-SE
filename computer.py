import random
from player import Player

class Computer(Player):
    """Class for a computer player."""
    def make_choice(self):
        """Randomly select Rock, Paper, or Scissors."""
        self.choice = random.choice(["rock", "paper", "scissors"])
        print(f"{self.name} chose {self.choice}")