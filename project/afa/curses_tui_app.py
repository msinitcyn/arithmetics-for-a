import traceback 
import curses
from .di_container_config import injector
from .main_view import MainView
from .yaml_task_level_template_reader import YamlTaskLevelTemplateReader
from .random_wrapper import RandomWrapper
from .task_level_builder import TaskLevelBuilder
from .task_builder import TaskBuilder
from .task_session import TaskSession
from .main_view_controller import MainViewController

class CursesTuiApp:
    def run(self):
        try:
            screen = curses.initscr()

            main_view = injector.get(MainView)
            main_view.init(screen)

            main_view_controller = injector.get(MainViewController)
            main_view_controller.start(main_view)
        except Exception as e:
            print("My exception handler: " + str(e))
            traceback.print_exc()

        finally:
            curses.endwin()

