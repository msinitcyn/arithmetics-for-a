class Task:
    def __init__(self, task_string: str, answer: str, full_task_string: str, numeric_answer: float):
        self.task_string = task_string
        self.answer = answer
        self.full_task_string = full_task_string
        self.numeric_answer = numeric_answer

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Task):
            return (
                self.task_string == other.task_string
                and self.answer == other.answer
                and self.full_task_string == other.full_task_string
                and self.numeric_answer == other.numeric_answer
            )
        return False

