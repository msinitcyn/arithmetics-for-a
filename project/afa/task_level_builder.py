from injector import inject
from .task_level_builder_abc import TaskLevelBuilderABC
from .task_level_template import TaskLevelTemplate
from .task_builder_abc import TaskBuilderABC
from .task_level import TaskLevel

class TaskLevelBuilder(TaskLevelBuilderABC):
    @inject
    def __init__(self, task_builder: TaskBuilderABC):
        self.task_builder = task_builder

    def build(self, template: TaskLevelTemplate) -> TaskLevel:
        tasks = self.task_builder.build(template)
        return TaskLevel(template.level_description, tasks)

