import unittest
from puzzles.Solution import Solution as sc

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = { 
        }
    
    def test_success(self):
        self.assertFalse(sc.Solution(self.test_cases['first'], True))

if __name__ == '__main__':
    unittest.main(verbosity=2)