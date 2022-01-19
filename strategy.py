from abc import ABC, abstractmethod

## Strategy interface 
class Strategy(ABC):
    @abstractmethod
    def selection(self) -> None:
        pass