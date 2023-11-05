from datetime import date
from dataclasses import dataclass

@dataclass
class LogItemModel:
    example: str
    date: date
    correct_answer: float
    actual_answer: float

