import curses
from typing import List
from .main_view_abc import MainViewABC
from .panel import Panel
from .task import Task

class MainView(MainViewABC):
    def init(self, screen):
        self._log_panel = Panel(screen, 40, 0, 20, 1000)
        self._log_panel.add_border(curses.COLOR_RED)

        self._task_panel = Panel(screen, 10, 0, 30, 2)
        self._task_panel.add_border(curses.COLOR_RED)

        self._status_panel = Panel(screen, 10, 10, 30, 30)
        self._status_panel.add_border(curses.COLOR_RED) 

    def redraw(self) -> None:
        self._log_panel.redraw()
        self._task_panel.redraw()

    def listen_for_user_answer(self) -> int:
        answer = None
        while answer == None:
            answer = self._task_panel.read_user_input(1,4)
        return answer

    def set_content(self, current_task: str) -> None:
        self._task_panel.set_content({current_task, answer_message, message}, 1, 1)

    def set_log(self, log: List[str]) -> None:
        self._log_panel.set_content(log, 1, 1)
