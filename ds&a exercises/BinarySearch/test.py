import unittest
from solution import Solution as target

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            { 
                'given':    ( [0,1,2,3,4,5,6,7,8,9], 0 ),
                'expected': 0 
            },
            { 
                'given':    ( [0], 3 ),
                'expected': -1
            },
            { 
                'given':    ( [0,4,5,8,9,100,105], 9 ),
                'expected': 4
            },
            { 
                'given':    ( [0,1], 1 ),
                'expected': 1
            },
        ]
    
    def test_solution(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.solution(*case['given']), case['expected'])
            # self.assertEqual(test.solution(case['given']), case['expected'])

if __name__ == '__main__':
    unittest.main(verbosity=2)