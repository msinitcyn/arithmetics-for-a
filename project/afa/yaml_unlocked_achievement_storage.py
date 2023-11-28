import os
import yaml

from typing import List
from .achievement import Achievement
from .unlocked_achievement_storage_abc import UnlockedAchievementStorageABC

class YamlUnlockedAchievementStorage(UnlockedAchievementStorageABC):

    def __init__(self, file_path: str):
        self._file_path = file_path

    def load_unlocked_achievements(self) -> List[Achievement]:
        unlocked_achievements = []
        if not os.path.exists(self._file_path):
            open(self._file_path, 'w').close()
        else:
            with open(self._file_path, 'r') as f:
                raw_items = yaml.safe_load(f) or []
                unlocked_achievements = [Achievement(**item) for item in raw_items]
        return unlocked_achievements

        
    def save_unlocked_achievements(self, achievements: List[Achievement]) -> None:
        items_list = [item.__dict__ for item in achievements]
        with open(self._file_path, 'w') as f:
            yaml.dump(items_list, f)

