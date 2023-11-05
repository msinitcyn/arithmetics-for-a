from typing import List
from .task import Task

class TaskLevel:
    def __init__(self, level_description: str, tasks: List[Task]):
        self.level_description = level_description
        self.tasks = tasks

