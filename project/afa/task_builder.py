from injector import inject
from typing import List
from .task_builder_abc import TaskBuilderABC
from .task import Task
from .task_level_template import TaskLevelTemplate
from .random_wrapper_abc import RandomWrapperABC

class TaskBuilder(TaskBuilderABC):
    @inject
    def __init__(self, random: RandomWrapperABC):
        self.random = random

    def build(self, template: TaskLevelTemplate) -> list[Task]:
        tasks = []
        for _ in range(template.task_count):
            operands = []
            for operand in template.operands:
                operand_value = self.random.randint(operand[0], operand[1])
                operands.append(str(operand_value))

            operators = self.random.choices(template.operators, k=len(operands) - 1)
            task_string = "".join([f"{operand} {operator} " for operand, operator in zip(operands, operators)] + [operands[-1]])
            numeric_answer = eval(task_string)
            answer = str(numeric_answer)
            full_task_string = task_string + " = " + answer

            task = Task(task_string, answer, full_task_string, numeric_answer)
            tasks.append(task)

        return tasks

