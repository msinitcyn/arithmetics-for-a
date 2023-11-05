from abc import ABC, abstractmethod
from typing import List
from .task import Task

class MainViewABC(ABC):
    @abstractmethod
    def redraw(self) -> None:
        pass

    @abstractmethod
    def listen_for_user_answer(self) -> None:
        pass

    @abstractmethod
    def set_log(self, log: List[str]) -> None:
        pass

    @abstractmethod
    def set_content(self, current_task: str) -> None:
        pass
