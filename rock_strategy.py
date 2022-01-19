from strategy import Strategy

## Concrete strategies
class Rock(Strategy):
    ## actual application will have the algorithm instead this method
    def selection(self) -> str:
        return "Rock"