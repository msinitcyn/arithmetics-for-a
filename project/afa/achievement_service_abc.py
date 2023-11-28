from abc import ABC, abstractmethod
from typing import List
from .achievement import Achievement

class AchievementServiceABC(ABC):

    @abstractmethod
    def unlock_achievements(self):
        pass

    @abstractmethod
    def get_unlocked_achievements(self) -> List[Achievement]:
        pass
