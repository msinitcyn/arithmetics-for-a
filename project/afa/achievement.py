from typing import List, Callable
from datetime import date
from .log_item_model import LogItemModel

class Achievement:
    def __init__(self, name: str, description: str, unlock_function: Callable[[List[LogItemModel]], bool]):
        self.name = name
        self.description = description
        self.unlock_function = unlock_function
        self.is_unlocked = False

    def unlock(self, log_items: List[LogItemModel]) -> bool:
        if not self.is_unlocked and self.unlock_function(log_items):
            self.is_unlocked = True
            self.unlocked_date = date.today(),
        return self.is_unlocked
