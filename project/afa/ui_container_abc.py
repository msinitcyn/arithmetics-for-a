from typing import List
from abc import ABC, abstractmethod

class UiContainerABC(ABC):
    @abstractmethod
    def set_content(self, text: List[str], x: int, y: int) -> None:
        pass

    @abstractmethod
    def read_user_input() -> str:
        pass
