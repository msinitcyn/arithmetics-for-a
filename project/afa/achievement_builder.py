from typing import List
from .achievement_builder_abc import AchievementBuilderABC
from .achievement import Achievement
from .log_item_model import LogItemModel

class AchievementBuilder(AchievementBuilderABC):

    def __init__(self):
        self._achievements = []
        self._achievements.append(Achievement("2-задачи", "🎉", "решил две задачи правильно", has_twenty_correct_answers))

    def build_achievements(self) -> List[Achievement]:
        return self._achievements

def has_twenty_correct_answers(log_items: List[LogItemModel]) -> bool:
    correct_answer_count = 0

    for log_item in log_items:
        if log_item.is_correct:
            correct_answer_count += 1

        if correct_answer_count >= 2:
            return True

    return False
