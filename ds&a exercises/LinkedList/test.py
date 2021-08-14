import unittest
from solution import Solution as target

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            { 
            'given':    10, 
            'expected': [10,11,12,13,14,15,16,17,18,19]
            },
            { 
            'given':    5, 
            'expected': [5,6,7,8,9]
            },
            { 
            'given':    1, 
            'expected': [1]
            },
            { 
            'given':    0, 
            'expected': []
            },
            { 
            'given':    -100, 
            'expected': []
            },
        ]
    
    def test_solution(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.solution(case['given']), case['expected'])

if __name__ == '__main__':
    unittest.main(verbosity=2)