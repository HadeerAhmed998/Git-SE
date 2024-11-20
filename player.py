class Player:
    """Base class for a player."""
    def __init__(self, name):
        self.name = name
        self.choice = None

    def make_choice(self):
        """Allow the player to choose Rock, Paper, or Scissors."""
        choices = ["rock", "paper", "scissors"]
        while True:
            self.choice = input(f"{self.name}, enter your choice (rock, paper, scissors): ").lower()
            if self.choice in choices:
                break
            print("Invalid choice. Please choose again.")