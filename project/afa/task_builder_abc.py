from abc import ABC, abstractmethod
from .task import Task
from .task_level_template import TaskLevelTemplate

class TaskBuilderABC(ABC):
    @abstractmethod
    def build(self, template: TaskLevelTemplate) -> list[Task]:
        pass

