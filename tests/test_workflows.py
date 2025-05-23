import unittest
from silk.workflows.example_workflow import run_example_workflow

class TestWorkflows(unittest.TestCase):

    def test_run_example_workflow(self):
        # Test the example workflow function
        result = run_example_workflow()
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, dict))  # Assuming the result is a dictionary

if __name__ == '__main__':
    unittest.main()