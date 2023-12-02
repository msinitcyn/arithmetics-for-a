from datetime import datetime
from dataclasses import dataclass

@dataclass
class LogItemModel:
    example: str
    datetime: datetime
    correct_answer: float
    actual_answer: float
    is_correct: bool = False
