import unittest
from puzzles.EasterEggs import Solution as target

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            { 
                'given':    [0, 14], 
                'expected': 0 
            },
            { 
                'given':    [2, 0], 
                'expected': 0 
            },
            { 
                'given':    [2, 14], 
                'expected': 105 
            },
            { 
                'given':    [7, 20], 
                'expected': 137979 
            },
        ]
    
    def test_solution(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.solution(*case['given']), case['expected'])

if __name__ == '__main__':
    unittest.main(verbosity=2)