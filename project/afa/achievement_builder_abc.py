from abc import ABC, abstractmethod
from typing import List
from .achievement import Achievement

class AchievementBuilderABC(ABC):

    @abstractmethod
    def build_achievements(self) -> List[Achievement]:
        pass
