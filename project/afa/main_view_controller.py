import time
from injector import inject
from .main_view_abc import MainViewABC
from .task_session_abc import TaskSessionABC

class MainViewController:
    @inject
    def __init__(self, main_view: MainViewABC, task_session: TaskSessionABC):
        self._main_view = main_view
        self._task_session = task_session

    def start(self):
        while True:
            self._current_task = self._task_session.get_next_task()
            self._main_view.set_content(f"{self._current_task.task_string} = ?")
            #self._main_view.set_log()
            self._main_view.redraw()
            answer = self._main_view.listen_for_user_answer()
            if answer == self._current_task.answer:
                message = "Молодец! Ты ответил правильно!"
            else:
                message = "Неправильно. Попробуй ещё"
            self._main_view.set_content(f"{self._current_task.task_string} = {self._current_task.answer}")
            time.sleep(2)
            self._task_session.answer_task(self._current_task, answer)
