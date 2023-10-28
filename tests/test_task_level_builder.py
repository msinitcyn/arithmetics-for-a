import sys
import os
import unittest

# Add the root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unittest.mock import Mock
from project.afa.task_level_builder import TaskLevelBuilder
from project.afa.task_level_template import TaskLevelTemplate
from project.afa.task_level import TaskLevel
from project.afa.task import Task

class TaskLevelBuilderTests(unittest.TestCase):
    def test_build(self):
        # Create a mock instance of TaskBuilderABC
        task_builder_mock = Mock()
        task_builder_mock.build.return_value = [
            Task(task_string="3 + 2", answer="5", full_task_string="3 + 2 = 5", numeric_answer=5),
            Task(task_string="4 - 5", answer="-1", full_task_string="4 - 5 = -1", numeric_answer=-1)
        ]

        # Create a TaskLevelTemplate
        template = TaskLevelTemplate(level_description="Level 1",
                                     operands=[(1, 10), (2, 5)],
                                     operators=["+", "-"],
                                     task_count=2)

        # Create an instance of TaskLevelBuilder with the mock TaskBuilderABC
        builder = TaskLevelBuilder(task_builder=task_builder_mock)

        # Call the build() method
        task_level = builder.build(template)

        # Check the result
        self.assertIsInstance(task_level, TaskLevel)
        self.assertEqual(task_level.level_description, "Level 1")
        self.assertEqual(len(task_level.tasks), 2)

        # Verify the mocked TaskBuilderABC method call
        task_builder_mock.build.assert_called_once_with(template)


if __name__ == '__main__':
    unittest.main()

