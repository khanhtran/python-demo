from strategy import Strategy


class Scissors(Strategy):
    def selection(self) -> str:
        return "Scissors"
