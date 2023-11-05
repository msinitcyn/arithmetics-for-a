from abc import ABC, abstractmethod
from .task_level_template import TaskLevelTemplate
from .task_level import TaskLevel

class TaskLevelBuilderABC(ABC):
    @abstractmethod
    def build(self, template: TaskLevelTemplate) -> TaskLevel:
        pass

