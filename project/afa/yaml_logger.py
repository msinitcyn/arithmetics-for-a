import os
import yaml
from typing import List, Optional

from .log_item_model import LogItemModel
from .logger_abc import LoggerABC

class YamlLogger(LoggerABC):
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._log_items = None  # Initialize local collection to None

    def _load_log_items(self) -> None:
        if not os.path.exists(self._file_path):
            # Create the file if it does not exist
            open(self._file_path, 'w').close()
            self._log_items = []
        else:
            with open(self._file_path, 'r') as f:
                log_items = yaml.safe_load(f) or []  # Handle empty file
                self._log_items = [LogItemModel(**item) for item in log_items]

    def _save_log_items(self) -> None:
        items_list = [item.__dict__ for item in self._log_items]
        with open(self._file_path, 'w') as f:
            yaml.dump(items_list, f)

    def append_log_item(self, log_item: LogItemModel) -> None:
        if self._log_items is None:
            self._load_log_items()

        self._log_items.append(log_item)
        self._save_log_items()

    def get_log(self, count: Optional[int] = None) -> List[LogItemModel]:
        if self._log_items is None:
            self._load_log_items()

        if count is None:
            return self._log_items

        return self._log_items[-min(count, len(self._log_items)):]
