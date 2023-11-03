import unittest
import sys
import os

# Add the root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unittest.mock import Mock, call
from project.afa.task_builder import TaskBuilder
from project.afa.task_level_template import TaskLevelTemplate
from project.afa.task import Task

class TaskBuilderTests(unittest.TestCase):
    def test_build(self):
        # Create a mock instance of RandomWrapperABC
        random_mock = Mock()
        random_mock.randint.side_effect = [3, 2, 4, 5]  # Mock the random number generation
        random_mock.choices.side_effect = [['+'], ['-']]

        # Create a TaskLevelTemplate
        template = TaskLevelTemplate(level_description="Level 1",
                                     operands=[(1, 10), (2, 5)],
                                     operators=["+", "-"],
                                     task_count=2)

        # Create an instance of TaskBuilder with the mock RandomWrapperABC
        builder = TaskBuilder(random=random_mock)

        # Call the build() method
        tasks = builder.build(template)

        # Check the results
        self.assertEqual(len(tasks), 2)  # Two tasks should be generated

        # Verify the mocked random number generation calls
        random_mock.randint.assert_has_calls([call(1, 10), call(2, 5), call(1, 10), call(2,5)])

        # Verify the generated tasks
        expected_tasks = [
            Task(task_string="3 + 2", answer="5", full_task_string="3 + 2 = 5", numeric_answer=5),
            Task(task_string="4 - 5", answer="-1", full_task_string="4 - 5 = -1", numeric_answer=-1)
        ]
        self.assertEqual(tasks, expected_tasks)


if __name__ == '__main__':
    unittest.main()
