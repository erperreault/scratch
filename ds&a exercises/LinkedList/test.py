import unittest
from solution import Solution as target

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            { 
            'given':    10, 
            'expected': [10,9,8,7,6,5,4,3,2,1,0]
            },
            { 
            'given':    0, 
            'expected': [0]
            },
            { 
            'given':    5, 
            'expected': [5,4,3,2,1,0]
            },
            { 
            'given':    1, 
            'expected': [1,0]
            },
        ]
    
    def test_solution(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.solution(case['given']), case['expected'])

if __name__ == '__main__':
    unittest.main(verbosity=2)