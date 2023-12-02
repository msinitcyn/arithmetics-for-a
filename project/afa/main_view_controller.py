import time
from injector import inject
from typing import List
from .main_view_abc import MainViewABC
from .task_session_abc import TaskSessionABC
from .logger_abc import LoggerABC
from .achievement_service_abc import AchievementServiceABC

class MainViewController:
    @inject
    def __init__(self, task_session: TaskSessionABC, logger: LoggerABC, achievement_service: AchievementServiceABC):
        self._task_session = task_session
        self._logger = logger
        self._achievement_service = achievement_service

    def start(self, main_view: MainViewABC):
        self._main_view = main_view

        while True:
            self._current_task = self._task_session.get_next_task()
            self._main_view.set_content(f"{self._current_task.task_string} = ")

            log_content = self._get_log_content()
            self._main_view.set_log(log_content)

            achievement_content = self._get_achievement_content()
            self._main_view.set_achievements(achievement_content)

            self._main_view.redraw()
            answer = self._main_view.listen_for_user_answer()

            self._task_session.answer_task(self._current_task, answer)
            self._achievement_service.unlock_achievements()

    def _get_log_content(self) -> List[str]:
        log = self._logger.get_log(12)
        log.reverse()
        transformed_list = []
        for index, log_item in enumerate(log, start=1):
            if log_item.is_correct:
                result_text = '✔️'
            else:
                result_text = '❌'
            first_line = f"{result_text} {log_item.example}"
            transformed_list.append(first_line)
        return transformed_list

    def _get_achievement_content(self) -> List[str]:
        achievements = self._achievement_service.get_unlocked_achievements()
        return [f"{item.icon} {item.name} - {item.description}" for item in achievements]
