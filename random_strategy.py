import random
from strategy import Strategy


class Random(Strategy):
    def selection(self) -> str:
        options = ["Rock", "Paper", "Scissors"]
        return random.choice(options)