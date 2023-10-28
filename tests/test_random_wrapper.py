import unittest
import sys
import os

# Add the root directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from project.afa.random_wrapper import RandomWrapper

class RandomWrapperTests(unittest.TestCase):
    def setUp(self):
        self.random = RandomWrapper()

    def test_randint(self):
        random_wrapper = RandomWrapper()
        result = random_wrapper.randint(1, 10)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 10)

    def test_choices_without_weights(self):
        population = ['a', 'b', 'c', 'd', 'e']
        result = self.random.choices(population, k=3)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(item in population for item in result))

    def test_choices_with_weights(self):
        population = ['a', 'b', 'c', 'd', 'e']
        weights = [1, 2, 3, 4, 5]
        result = self.random.choices(population, weights=weights, k=3)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(item in population for item in result))

if __name__ == '__main__':
    unittest.main()

