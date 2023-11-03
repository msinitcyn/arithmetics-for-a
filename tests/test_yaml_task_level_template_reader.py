import unittest
import sys
import os

# Add the root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from project.afa.yaml_task_level_template_reader import YamlTaskLevelTemplateReader

class YamlTaskLevelTemplateReaderTests(unittest.TestCase):
    def test_read_valid_file(self):
        reader = YamlTaskLevelTemplateReader()
        templates = reader.read('templates.yaml')

        self.assertEqual(len(templates), 2)

        template1 = templates[0]
        self.assertEqual(template1.level_description, "Level 1")
        self.assertEqual(template1.task_count, 5)
        self.assertEqual(template1.operands, [(1, 10), (3, 5)])
        self.assertEqual(template1.operators, ['+', '-'])

        template2 = templates[1]
        self.assertEqual(template2.level_description, "Level 2")
        self.assertEqual(template2.task_count, 10)
        self.assertEqual(template2.operands, [(6, 9), (1, 1), (5, 9)])
        self.assertEqual(template2.operators, ['*', '+'])

if __name__ == '__main__':
    unittest.main()
