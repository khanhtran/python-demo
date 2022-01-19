## Changing the strategy among Rock, Paper, Scissors, and Random
import random
from strategy import Strategy
from random_strategy import Random
from paper_strategy import Paper
from rock_strategy import Rock
from scissor_strategy import Scissors


class Random(Strategy):
    def selection(self) -> str:
        options = ["Rock", "Paper", "Scissors"]
        return random.choice(options)

## Context class
class Game:
    strategy: Strategy

    def __init__(self, strategy: Strategy = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Random()

    def play(self, sec) -> None:
        s1 = self.strategy.selection()
        s2 = sec.strategy.selection()
        if s1 == s2:
            print("It's a tie")
        elif s1 == "Rock":
            if s2 == "Scissors":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
        elif s1 == "Scissors":
            if s2 == "Paper":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
        elif s1 == "Paper":
            if s2 == "Rock":
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")

## Example application
## PLayer 1 can select his strategy

strategies = {
    'paper': Paper(),
    'rock': Rock(),
    'random': Random(),
    'scisor': Scissors()
}
player1 = Game(strategies['paper'])

# Player 2 gets to select
player2 = Game(strategies['rock'])

# After the second player choice, we call the play method
player1.play(player2)