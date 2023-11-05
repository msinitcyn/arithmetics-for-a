from abc import ABC, abstractmethod
from .task import Task

class TaskProviderABC(ABC):
    @abstractmethod
    def get_next_task(self) -> Task:
        pass

