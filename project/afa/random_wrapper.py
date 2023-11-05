import random
from .random_wrapper_abc import RandomWrapperABC

class RandomWrapper(RandomWrapperABC):
    def randint(self, a: int, b: int) -> int:
        return random.randint(a, b)

    def choices(self, population, weights=None, k=1):
        return random.choices(population, weights=weights, k=k)
