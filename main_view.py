import curses
import msvcrt

class MainView:
    def __init__(self):
        self.screen = curses.initscr()
        self.screen_cols = curses.COLS
        self.screen_lines = curses.LINES

        self.WIDTH = min(self.screen_cols, 100)
        self.HEIGHT = min(self.screen_lines, 30)

        self.top = (self.screen_lines - self.HEIGHT)//2
        self.left = (self.screen_cols - self.WIDTH)//2

        self.right_panel_width = 30
        self.title_height = 10
        self.history_heght = 20

        self.left_shift = 10
        self.top_shift = 1

        self.screen.clear()

    def __draw_frame__(self):
        for i in range(self.WIDTH):
            self.screen.addstr(self.top, self.left + i, "━")
            self.screen.addstr(self.top + self.HEIGHT, self.left + i, "━")

        for i in range(self.HEIGHT):
            self.screen.addstr(self.top + i, self.left, "│")
            self.screen.addstr(self.top + i, self.left + self.WIDTH, "│")
            self.screen.addstr(self.top + i, self.left + self.WIDTH - self.right_panel_width, "│")

        self.screen.addstr(self.top, self.left, "┌")
        self.screen.addstr(self.top, self.left + self.WIDTH, "┑")
        self.screen.addstr(self.top + self.HEIGHT, self.left, "└")
        self.screen.addstr(self.top + self.HEIGHT, self.left + self.WIDTH, "┘")
        self.screen.addstr(self.top, self.left + self.WIDTH - self.right_panel_width, "┬")
        self.screen.addstr(self.top + self.HEIGHT, self.left + self.WIDTH - self.right_panel_width, "┴")

    def __draw_title_section__(self):
        for i in range(self.WIDTH - self.right_panel_width):
            self.screen.addstr(self.top + self.title_height, self.left + i, "━")

        self.screen.addstr(self.top + self.title_height, self.left, "├")
        self.screen.addstr(self.top + self.title_height, self.left + self.WIDTH - self.right_panel_width, "┤")

    def __draw_log__(self, task_log_list):
        line = 1
        for i in task_log_list[:-10]:
            task_log_item = i
            self.screen.addstr(self.top + line, self.left + self.WIDTH - self.right_panel_width + 1, task_log_item['task'])
            line += 1

    def draw(self, task_log_list, text, input_validator):
        while True:
            self.screen.clear()

            self.__draw_frame__()
            self.__draw_title_section__()

            self.__draw_log__(task_log_list)

            cur_col = self.left + self.left_shift
            cur_line = self.top + self.top_shift

            text_height = min(len(text), self.HEIGHT)
            for x in range(text_height):
                self.screen.addstr(cur_line, cur_col, text[x])
                cur_line += 1
            self.screen.refresh()
            user_input = self.screen.getstr(cur_line, cur_col, 20).decode("utf-8")
            if input_validator(user_input):
                return user_input
            #curses.echo()

#def handler(s:str):
#    print(s)

#mainView = MainView()
#mainView.draw("some string", handler)
#input_char = msvcrt.getch()
