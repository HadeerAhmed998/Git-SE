class Game:
    """Class to handle the Rock, Paper, Scissors game logic."""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def determine_winner(self):
        """Determine the winner based on player choices."""
        if self.player1.choice == self.player2.choice:
            return "It's a tie!"

        # Winning combinations
        wins = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

        if wins[self.player1.choice] == self.player2.choice:
            return f"{self.player1.name} wins!"
        else:
            return f"{self.player2.name} wins!"

    def play(self):
        """Run the game."""
        print("Welcome to Rock, Paper, Scissors!")
        self.player1.make_choice()
        self.player2.make_choice()
        result = self.determine_winner()
        print(result)