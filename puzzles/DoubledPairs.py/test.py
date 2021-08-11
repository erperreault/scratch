import unittest
from solution import Solution as target

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            { 
                'given':    [1,2,4,16,8,4], 
                'expected': False
            },
            { 
                'given':    [3,1,3,6], 
                'expected': False
            },
            { 
                'given':    [4,-2,2,-4], 
                'expected': True
            },
        ]
    
    def test_solution(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.solution(case['given']), case['expected'])

if __name__ == '__main__':
    unittest.main(verbosity=2)