import unittest
from src import helpers

class TestHelpers(unittest.TestCase):

    def test_is_fancode_city(self):
        self.assertTrue(helpers.is_fancode_city(0, 50))   # Test with valid coordinates
        self.assertFalse(helpers.is_fancode_city(-50, 50))  # Invalid latitude
        self.assertFalse(helpers.is_fancode_city(0, 150))   # Invalid longitude

    def test_calculate_task_completion(self):
        todos = [
            {"completed": True},
            {"completed": False},
            {"completed": True}
        ]
        self.assertEqual(round(helpers.calculate_task_completion(todos), 2), 66.67)  # Test task completion percentage

if __name__ == "__main__":
    unittest.main()
