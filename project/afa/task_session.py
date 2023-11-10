from injector import inject
from collections import deque
from datetime import date
from .logger_abc import LoggerABC
from .log_item_model import LogItemModel
from .task_session_abc import TaskSessionABC
from .task_level_template_reader_abc import TaskLevelTemplateReaderABC
from .task_level_builder_abc import TaskLevelBuilderABC
from .task import Task
from .panel import Panel
from .event import Event

class TaskSession(TaskSessionABC):
    @inject
    def __init__(
        self,
        logger: LoggerABC,
        task_level_template_reader: TaskLevelTemplateReaderABC,
        task_level_builder: TaskLevelBuilderABC
    ):
        self._template_file = "templates.yaml"

        self._logger = logger
        self._log = logger.read_log()
        self._task_level_template_reader = task_level_template_reader
        self._task_level_builder = task_level_builder
        self._tasks = None
        self._current_task = None

    def _read_new_tasks(self) -> deque:
        templates = self._task_level_template_reader.read(self._template_file)
        self._tasks = deque()
        for template in templates:
            task_level = self._task_level_builder.build(template)
            for task in task_level.tasks:
                self._tasks.append(task)

    def answer_task(self, task: Task, answer: float) -> None:
        logItem = LogItemModel(
            example=task.full_task_string,
            date=date.today(),
            correct_answer=task.answer,
            actual_answer=str(answer))
        self._log.append(logItem)
        self._logger.save_log(self._log)

    def get_next_task(self) -> Task:
        if not self._tasks:
            self._read_new_tasks()
        return self._tasks.popleft()

    def get_log(self):
        return self._log
