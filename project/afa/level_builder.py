import random
from random import randrange

class LevelOne():

    def __init__(self, level_number):
        self.level_number = level_number

    def get_task_description(self):

class LevelFive():

    def __init__(self, level_number):
        self.level_number = level_number

    def get_task_description(self):
        return "Уровень {}. Двойное сложение.".format(self.level_number)

    def get_task(self):
        operand1 = randrange(5) + 5
        operand2 = randrange(5)
        operand3 = randrange(5)
        task_result = operand1 + operand2 + operand3
        task_string = "{} + {} + {} = ?".format(operand1, operand2, operand3)
        return task_result, task_string

class LevelSix():

    def __init__(self, level_number):
        self.level_number = level_number

    def get_task_description(self):
        return "Уровень {}. Сложение и вычитание.".format(self.level_number)

    def get_task(self):
        operand1 = randrange(5) + 5
        operand2 = randrange(5)
        operand3 = randrange(5)
        task_result = operand1 + operand2 - operand3
        task_string = "{} + {} - {} = ?".format(operand1, operand2, operand3)
        return task_result, task_string

class LevelSeven():

    def __init__(self, level_number):
        self.level_number = level_number

    def get_task_description(self):
        return "Уровень {}. Трудное двойное сложение.".format(self.level_number)

    def get_task(self):
        operand1 = randrange(5) + 5
        operand2 = randrange(5) + 5
        operand3 = randrange(5) + 5
        task_result = operand1 + operand2 + operand3
        task_string = "{} + {} + {} = ?".format(operand1, operand2, operand3)
        return task_result, task_string

class LevelEight():

    def __init__(self, level_number):
        self.level_number = level_number

    def get_task_description(self):
        return "Уровень {}. Трудное сложение и вычитание.".format(self.level_number)

    def get_task(self):
        operand1 = randrange(5) + 5
        operand2 = randrange(5) + 5
        operand3 = max(operand1 + operand2)
        task_result = operand1 + operand2 - operand3
        task_string = "{} + {} - {} = ?".format(operand1, operand2, operand3)
        return task_result, task_string

class TaskBuilder():

    def __init__(self):
        self.levels = [LevelOne(1), LevelTwo(2), LevelThree(3), LevelFour(4), LevelFive(5), LevelSix(6), LevelSeven(7), LevelEight(8)]
        self.cur_level_index = 0
        self.cur_task = 0
        self.tasks_per_level = 10

    def get_next_task(self):
        cur_level = self.levels[self.cur_level_index]
        level_description = cur_level.get_task_description()
        task_result, task_string = cur_level.get_task()
        self.cur_task += 1
        if self.cur_task == self.tasks_per_level:
            self.cur_task = 0
            self.cur_level_index += 1

        is_last_task = False
        if self.cur_level_index > len(self.levels):
            is_last_task = True

        return level_description, task_result, task_string, is_last_task
