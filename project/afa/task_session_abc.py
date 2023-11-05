from abc import ABC, abstractmethod
from .task import Task

class TaskSessionABC(ABC):
    @abstractmethod
    def answer_task(self, task: Task, answer: float) -> None:
        pass

    @abstractmethod
    def get_next_task(self) -> Task:
        pass

    @abstractmethod
    def get_log(self):
        pass
