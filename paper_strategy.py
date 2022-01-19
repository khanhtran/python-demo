from strategy import Strategy

## Concrete strategies
class Paper(Strategy):
    ## actual application will have the algorithm instead this method
    def selection(self) -> str:
        return "Paper"