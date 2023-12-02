from datetime import datetime
from dataclasses import dataclass

@dataclass
class UnlockedAchievementModel:
    name: str
    unlocked_datetime: datetime
