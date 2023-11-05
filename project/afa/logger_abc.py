from abc import ABC, abstractmethod
from typing import List
from .log_item_model import LogItemModel

class LoggerInterface(ABC):
    @abstractmethod
    def read_log(self) -> List[LogItemModel]:
        pass
    
    @abstractmethod
    def save_log(self, logitems: List[LogItemModel]) -> None:
        pass

