from player import Player
from computer import Computer
from game import Game

def main():
    # Create Players
    player1 = Player("Player 1")
    player2 = Computer("Computer")

    # Create Game
    game = Game(player1, player2)
    game.play()

if __name__ == "__main__":
    main()
