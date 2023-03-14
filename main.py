import curses
import json
import msvcrt
from datetime import date
from enum import auto, Enum, verify, UNIQUE
from random import randrange
import random
from main_view import MainView
from level_builder import TaskBuilder
from task_logger import TaskLogger

@verify(UNIQUE)
class ArithmeticOperator(Enum):
    PLUS = auto()
    MINUS = auto()

    def __str__(self):
        result = ""
        if self == ArithmeticOperator.PLUS:
            result = "+"
        if self == ArithmeticOperator.MINUS:
            result = "-"
        return result

    def calculate(self, operand_1, operand_2)->int:
        result = operand_1
        if self == ArithmeticOperator.PLUS:
            result = operand_1 + operand_2
        if self == ArithmeticOperator.MINUS:
            result = operand_1 - operand_2
        return result

def load_record()->int:
    result = 0
    with open(record_file) as f:
        result = json.load(f)

    return result

def save_record(record: int):
    with open(record_file, 'w') as f:
        json.dump(record, f)

def validate_int(user_input)->bool:
    return user_input.isnumeric()

def validate_anything(user_input)->bool:
    return True

def play_game(greeting, task_builder):
    log_item_list = logger.read()
    text_to_show = greeting
    solved = 0
    while True: 
        (level_description, expected, task_string, is_last_task) = task_builder.get_next_task()
        text_to_show += [level_description]
        if is_last_task:
            text_to_show += ["Внимание! Это последнее задание в игре!"]
        text_to_show += [task_string]
        actual = main_view.draw(log_item_list, text_to_show, validate_int)
        task_log_item = {'task': task_string, 'expected':expected, 'actual':actual};
        logger.append(task_log_item)
        text_to_show = []
        if expected != int(actual):
            text_to_show += ["Ошибка. Правильный ответ: {}. Всего правильных ответов: {}".format(expected, solved)]
            if solved > record:
                text_to_show += ["Поздравляю! Новый рекорд: {}!".format(solved)]
            main_view.draw(log_item_list, text_to_show, validate_anything)
            break

        else:
            solved += 1
            text_to_show += ["Правильно! Уже правильных ответов: {}".format(solved)]
            if solved > record:
                save_record(solved)
                text_to_show += ["... и это новый рекорд!"]

        if is_last_task:
            text_to_show = ["Поздравляю! Ты прошёл игру!"]

main_view = MainView()
logger = TaskLogger("taskLog.yaml")

task_builder = TaskBuilder()

record_file = 'record.txt'

record = load_record()
greeting = ["Привет!", "Твой предыдущий рекорд: {}".format(record), "Поехали!"]

play_game(greeting, task_builder)
