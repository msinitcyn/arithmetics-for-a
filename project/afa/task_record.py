from .task import Task

class TaskRecord:
    def __init__(self, task: Task, user_answer: float, is_correct: bool):
        self.task = task
        self.user_answer = user_answer
        self.is_correct = is_correct

