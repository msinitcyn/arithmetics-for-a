from injector import Injector
from .task_level_template_reader_abc import TaskLevelTemplateReaderABC
from .yaml_task_level_template_reader import YamlTaskLevelTemplateReader
from .random_wrapper_abc import RandomWrapperABC
from .random_wrapper import RandomWrapper
from .task_level_builder_abc import TaskLevelBuilderABC
from .task_level_builder import TaskLevelBuilder
from .task_builder_abc import TaskBuilderABC
from .task_builder import TaskBuilder
from .main_view_abc import MainViewABC
from .main_view import MainView
from .task_session_abc import TaskSessionABC
from .task_session import TaskSession
from .logger_abc import LoggerABC
from .yaml_logger import YamlLogger
from .achievement_builder_abc import AchievementBuilderABC
from .achievement_builder import AchievementBuilder
from .unlocked_achievement_storage_abc import UnlockedAchievementStorageABC
from .yaml_unlocked_achievement_storage import YamlUnlockedAchievementStorage
from .achievement_service_abc import AchievementServiceABC
from .achievement_service import AchievementService

injector = Injector()
injector.binder.bind(TaskLevelTemplateReaderABC, to=YamlTaskLevelTemplateReader)
injector.binder.bind(RandomWrapperABC, to=RandomWrapper)
injector.binder.bind(TaskLevelBuilderABC, to=TaskLevelBuilder)
injector.binder.bind(TaskBuilderABC, to=TaskBuilder)
injector.binder.bind(MainViewABC, to=MainView)
injector.binder.bind(TaskSessionABC, to=TaskSession)
injector.binder.bind(LoggerABC, to=YamlLogger("log.yaml"))
injector.binder.bind(AchievementBuilderABC, to=AchievementBuilder)
injector.binder.bind(UnlockedAchievementStorageABC, to=YamlUnlockedAchievementStorage("achievements.yaml"))
injector.binder.bind(AchievementServiceABC, to=AchievementService)
