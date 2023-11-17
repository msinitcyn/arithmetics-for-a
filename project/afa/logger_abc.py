from abc import ABC, abstractmethod
from typing import List
from .log_item_model import LogItemModel

class LoggerABC(ABC):
    @abstractmethod
    def append_log_item(self, log_item: LogItemModel) -> None:
        pass
    
    @abstractmethod
    def get_log(self, count: int) -> List[LogItemModel]:
        pass

