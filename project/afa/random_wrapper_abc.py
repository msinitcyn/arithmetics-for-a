from abc import ABC, abstractmethod

class RandomWrapperABC(ABC):
    @abstractmethod
    def randint(self, a: int, b: int) -> int:
        pass

    def choices(self, population, weights=None, k=1):
        pass
