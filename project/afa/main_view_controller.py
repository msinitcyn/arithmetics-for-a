import time
from injector import inject
from .main_view_abc import MainViewABC
from .task_session_abc import TaskSessionABC

class MainViewController:
    @inject
    def __init__(self, main_view: MainViewABC, task_session: TaskSessionABC):
        self._main_view = main_view
        self._task_session = task_session
        self._status = []

    def start(self):
        while True:
            self._current_task = self._task_session.get_next_task()
            self._main_view.set_content(f"{self._current_task.task_string} = ?")
            self._main_view.set_status(self._status)

            log = self._task_session.get_log()
            log.reverse()
            transformed_list = []
            for index, log_item in enumerate(log, start=1):
                if int(float(log_item.actual_answer)) == int(float(log_item.correct_answer)):
                    result_text = "Правильно"
                else:
                    result_text = "Неправильно"
                first_line = f"{index}. {log_item.example}"
                transformed_list.append(first_line)
                second_line = f"Твой ответ: {int(float(log_item.actual_answer))} - {result_text}"
                transformed_list.append(second_line)
                transformed_list.append("")
            self._main_view.set_log(transformed_list)
            self._main_view.redraw()
            answer = self._main_view.listen_for_user_answer()

            self._status = []
            self._status.append("Предыдущий пример:")
            self._status.append(f"{self._current_task.task_string} = {self._current_task.answer}")
            self._status.append(f"Твой ответ: {int(answer)}")
            if int(answer) == int(self._current_task.answer):
                self._status.append("Молодец!")
            else:
                self._status.append("Неправильно. Попробуй ещё")

            self._task_session.answer_task(self._current_task, answer)
