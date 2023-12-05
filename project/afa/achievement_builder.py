from typing import List
from datetime import datetime, timedelta
from .achievement_builder_abc import AchievementBuilderABC
from .achievement import Achievement
from .log_item_model import LogItemModel

class AchievementBuilder(AchievementBuilderABC):

    def __init__(self):
        self._achievements = []
        self._achievements.append(Achievement("Начало", "👶", "Решил 20 задач правильно", has_20_correct_answers))
        self._achievements.append(Achievement("Неделя", "🤪", "Правильный ответ в каждый день недели", week_of_correct_answers))
        self._achievements.append(Achievement("Упорство", "👑", "Решил 20 задач правильно за один день", at_least_20_correct_answers_last_day))
        self._achievements.append(Achievement("Калькулятор", "🎓", "Решил 100 задач подряд", at_least_100_correct_answers_in_a_row))

    def build_achievements(self) -> List[Achievement]:
        return self._achievements

def has_20_correct_answers(log_items: List[LogItemModel]) -> bool:
    recent_log_items = log_items[-20:]
    return sum(1 for log_item in recent_log_items if log_item.is_correct) >= 20

def week_of_correct_answers(log_items: List[LogItemModel]) -> bool:
    today = datetime.today()
    last_week_start = today - timedelta(days=7)

    recent_log_items = [log_item for log_item in log_items if last_week_start <= log_item.datetime <= today]

    unique_dates = set(log_item.datetime.date() for log_item in recent_log_items)
    return all(any(log_item.is_correct for log_item in recent_log_items if log_item.datetime.date() == date) for date in unique_dates)

def at_least_20_correct_answers_last_day(log_items: List[LogItemModel]) -> bool:
    today = datetime.today()
    last_day = today - timedelta(days=1)

    last_day_log_items = [log_item for log_item in log_items if log_item.datetime.date() == last_day.date()]
    
    return len([log_item for log_item in last_day_log_items if log_item.is_correct]) >= 20

def at_least_100_correct_answers_in_a_row(log_items: List[LogItemModel]) -> bool:
    recent_log_items = log_items[-100:]
    correct_count = 0

    for log_item in reversed(recent_log_items):
        if log_item.is_correct:
            correct_count += 1
        else:
            correct_count = 0

        if correct_count >= 100:
            return True

    return False

