import curses
from typing import List
from .ui_container_abc import UiContainerABC
from .label import Label

class Panel(UiContainerABC):
    def __init__(self, screen, x: int, y: int, width: int, height: int):
        self._screen = screen
        self._height = height
        self._width = width
        self._x = x
        self._y = y

        if self.actual_height > 0 and self.actual_width > 0:
            self._window = curses.newwin(self.actual_height, self.actual_width, self.actual_y, self.actual_x)

        self._content = []
        self.border_color = None

    @property
    def actual_width(self) -> int:
        if self._width == 0:
            return curses.COLS
        else:
            return min(max(0, curses.COLS - self.actual_x), self._width)

    @property
    def actual_height(self) -> int:
        if self._height == 0:
            return curses.LINES
        else:
            return min(max(0, curses.LINES - self.actual_y), self._height)

    @property
    def actual_x(self) -> int:
        return min(curses.COLS, self._x)

    @property
    def actual_y(self) -> int:
        return min(curses.LINES, self._y)

    def set_content(self, text: List[str], x: int, y: int) -> None:
        self._content = []
        for i, item in enumerate(text):
            self._content.append(Label(item, x, y+i))

    def add_border(self, color: int) -> None:
        self.border_color = color
        self._window.border()

    def read_user_input(self, x, y) -> str:
        content = self._content
        max_input_size = 10
        input_str = ""
        result = ""
        input_label = Label("", x, y)

        while True:
            input_label.content = input_str
            self._content = content
            self._content.append(input_label)
            self.redraw()

            key = self._window.getch()

            if key == 10:  # Enter key
                result = self._convert_string_to_float(input_str.strip())
                if result is not None:
                    break
            elif key == curses.KEY_BACKSPACE or key == 127:  # Backspace
                input_str = input_str[:-1]
            elif key == 3:  # Ctrl+C
                raise KeyboardInterrupt
            elif key == 45 and len(input_str) == 0:  # '-' (minus) as the first character
                input_str += "-"
            elif 48 <= key <= 57:  # Numeric characters (ASCII codes 48-57)
                if len(input_str) < max_input_size:
                    input_str += chr(key)

        return result

    def _convert_string_to_float(self, s: str) -> float:
        try:
            return float(s)
        except ValueError:
            return None

    def redraw(self) -> None:
        self._window.clear()

        if self.border_color is not None:
            self._window.border()

        for line in self._content:
            y = min(line.y, self.actual_height - 2)
            x = min(line.x, self.actual_width - 2)
            max_width = max(0, self.actual_width - line.x - 2)
            self._window.addstr(y, x, ' ' * (self.actual_width-x-1))
            self._window.addstr(y, x, line.content[:max_width])

        self._window.refresh()

