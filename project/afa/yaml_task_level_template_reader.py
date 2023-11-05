import yaml
from .task_level_template import TaskLevelTemplate
from .task_level_template_reader_abc import TaskLevelTemplateReaderABC


class YamlTaskLevelTemplateReader(TaskLevelTemplateReaderABC):
    def read(self, filename):
        templates = []
        with open(filename, 'r') as file:
            data = yaml.safe_load(file)
            for item in data:
                level_description = item.get('level_description')
                task_count = item.get('task_count')
                operands = [tuple(op) for op in item['operands']]
                operators = item.get('operators')
                templates.append(TaskLevelTemplate(level_description, operands, operators, task_count))
        return templates

