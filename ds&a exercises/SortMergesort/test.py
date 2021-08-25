import unittest
from solution import Solution as target

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            { 
                'given':    [9,4,7,3,2,1,5,6,8,0], 
                'expected': [0,1,2,3,4,5,6,7,8,9] 
            },
        ]
    
    def test_solution(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.solution(case['given']), case['expected'])

if __name__ == '__main__':
    unittest.main(verbosity=2)