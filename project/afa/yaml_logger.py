from typing import List
import os
import yaml

from .log_item_model import LogItemModel
from .logger_abc import LoggerABC

class YamlLogger(LoggerABC):
    def __init__(self, file_path: str):
        self._file_path = file_path

    def read_log(self) -> List[LogItemModel]:
        if not os.path.exists(self._file_path):
            return []  # File does not exist, return an empty list

        with open(self._file_path, 'r') as f:
            log_items = yaml.safe_load(f) or []  # Handle empty file
            return [LogItemModel(**item) for item in log_items]

    def save_log(self, log_items: List[LogItemModel]) -> None:
        items_list = [item.__dict__ for item in log_items]
        with open(self._file_path, 'w') as f:
            yaml.dump(items_list, f)
