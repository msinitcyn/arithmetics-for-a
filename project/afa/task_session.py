from injector import inject
from collections import deque
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
        task_level_template_reader: TaskLevelTemplateReaderABC,
        task_level_builder: TaskLevelBuilderABC
    ):
        self._task_level_template_reader = task_level_template_reader
        self._task_level_builder = task_level_builder
        self._tasks = None
        self._current_task = None
        self._template_file = "templates.yaml"

    def _read_new_tasks(self) -> deque:
        templates = self._task_level_template_reader.read(self._template_file)
        self._tasks = deque()
        for template in templates:
            task_level = self._task_level_builder.build(template)
            for task in task_level.tasks:
                self._tasks.append(task)

    def answer_task(self, task: Task, answer: float) -> None:
        pass

    def get_next_task(self) -> Task:
        if not self._tasks:
            self._read_new_tasks()
        return self._tasks.popleft()

    def get_log(self):
        pass
