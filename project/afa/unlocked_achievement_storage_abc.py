from abc import ABC, abstractmethod
from typing import List
from .achievement import Achievement

class UnlockedAchievementStorageABC(ABC):

    @abstractmethod
    def load_unlocked_achievements(self) -> List[Achievement]:
        pass

    @abstractmethod
    def save_unlocked_achievements(self, achievements: List[Achievement]) -> None:
        pass
