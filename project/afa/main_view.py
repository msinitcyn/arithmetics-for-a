import curses
from typing import List
from .main_view_abc import MainViewABC
from .panel import Panel
from .task import Task

class MainView(MainViewABC):
    def init(self, screen):

        self._header_panel = Panel(screen, 40, 1, 57, 9)
        self._header_panel.set_content([
'  /$$$$$$         /$$$$$$       /$$$$  /$$$$  /$$$$ ',
' /$$__  $$  /$$  /$$__  $$     /$$  $$/$$  $$/$$  $$',
'|__/  \ $$ | $$ |__/  \ $$/$$$|__/\ $|__/\ $|__/\ $$',
'  /$$$$$$/$$$$$$$$/$$$$$$|____/   /$$/   /$$/   /$$/',
' /$$____|__  $$__/$$____/ /$$$$  /$$/   /$$/   /$$/ ',
'| $$       | $$ | $$     |____/ |__/   |__/   |__/  ',
'| $$$$$$$$ |__/ | $$$$$$$$       /$$    /$$    /$$  ',
'|________/      |________/      |__/   |__/   |__/  '],1,1)

        self._log_panel = Panel(screen, 70, 10, 25, 16)
        self._log_panel.add_border(curses.COLOR_RED)
        self._log_panel_title = 'История:'

        self._task_panel = Panel(screen, 40, 10, 30, 6)
        self._x_coordinate_for_input = 1
        self._task_panel.add_border(curses.COLOR_RED)
        self._task_panel_title = 'Реши:'

        self._status_panel = Panel(screen, 40, 16, 30, 10)
        self._status_panel.add_border(curses.COLOR_RED) 
        self._status_panel_title = 'Статус:'

        self._achievement_panel = Panel(screen, 40, 26, 55, 10)
        self._achievement_panel.add_border(curses.COLOR_RED)
        self._achievement_panel.title = 'Достижения:'

    def redraw(self) -> None:
        self._header_panel.redraw()
        self._log_panel.redraw()
        self._task_panel.redraw()
        self._status_panel.redraw()
        self._achievement_panel.redraw()

    def listen_for_user_answer(self) -> int:
        answer = None
        while answer == None:
            answer = self._task_panel.read_user_input(self._x_coordinate_for_input, 3)
        return answer

    def set_content(self, current_task: str) -> None:
        self._x_coordinate_for_input = len(current_task)+1
        self._task_panel.set_content([self._task_panel_title, '', current_task], 1, 1)

    def set_status(self, status: List[str]) -> None:
        self._status_panel.set_content([self._status_panel_title, ''] + status, 1, 1)

    def set_log(self, log: List[str]) -> None:
        self._log_panel.set_content([self._log_panel_title, ''] + log, 1, 1)
