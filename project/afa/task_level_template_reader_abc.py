from abc import ABC, abstractmethod
from typing import List
from .task_level_template import TaskLevelTemplate

class TaskLevelTemplateReaderABC(ABC):
    @abstractmethod
    def read(self, filename: str) -> List[TaskLevelTemplate]:
        pass

