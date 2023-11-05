from Task import Task

class TaskProvider:
    def __init__(self):
        self.tasks = []  # List of Task objects

    def get_next_task(self) -> Task:
        # Implement logic to retrieve the next task
        # For this example, let's assume the tasks are stored in a list
        if len(self.tasks) > 0:
            return self.tasks.pop(0)
        else:
            # Return None or raise an exception if there are no more tasks
            return None

