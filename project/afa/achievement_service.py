import curses
from injector import inject
from typing import List
from .logger_abc import LoggerABC
from .achievement import Achievement
from .unlocked_achievement_model import UnlockedAchievementModel
from .achievement_service_abc import AchievementServiceABC
from .achievement_builder_abc import AchievementBuilderABC
from .unlocked_achievement_storage_abc import UnlockedAchievementStorageABC

class AchievementService(AchievementServiceABC):

    @inject
    def __init__(self, logger: LoggerABC, achievement_builder: AchievementBuilderABC, unlocked_achievement_storage: UnlockedAchievementStorageABC):
        self._logger = logger
        self._achievement_builder = achievement_builder
        self._unlocked_achievement_storage = unlocked_achievement_storage
        self._locked_achievements = []
        self._unlocked_achievements = []

    def unlock_achievements(self):
        log = self._logger.get_log()
        need_to_update_unlocked_achievements = False
        for achievement in self._locked_achievements.copy():
            if achievement.unlock(log):
                #curses.endwin()
                #breakpoint()
                self._locked_achievements.remove(achievement)
                self._unlocked_achievements.append(achievement)
                need_to_update_unlocked_achievements = True

        if need_to_update_unlocked_achievements:
            unlocked_achievements = [
                UnlockedAchievementModel(name=unlocked_achievement.name, unlocked_datetime=unlocked_achievement.unlocked_datetime)
                for unlocked_achievement in self._unlocked_achievements
            ]
            self._unlocked_achievement_storage.save_unlocked_achievements(unlocked_achievements)

    def get_unlocked_achievements(self) -> List[Achievement]:
        if self._locked_achievements == [] and self._unlocked_achievements == []:
            self._load_achievements()
        return self._unlocked_achievements

    def _load_achievements(self) -> None:
        all_achievements = self._achievement_builder.build_achievements()
        unlocked_achievement_models = self._unlocked_achievement_storage.load_unlocked_achievements()

        for achievement in all_achievements:
            matching_unlocked = next((unlocked_achievement for unlocked_achievement_model in unlocked_achievement_models
               if unlocked_achievement_model.name == achievement.name), None)

            if matching_unlocked:
                achievement.is_unlocked = True
                achievement.unlocked_date = matching_unlocked.unlocked_date
                self._unlocked_achievements.append(achievement)
            else:
                self._locked_achievements.append(achievement)
