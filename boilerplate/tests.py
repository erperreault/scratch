import unittest
from ..puzzles import puzzle

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = { 
        }
    
    def test_success(self):
        self.assertFalse(self.test_cases)

if __name__ == '__main__':
    unittest.main(verbosity=2)