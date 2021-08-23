import unittest
from solution import Solution as target

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            { 
                'given':    ([0,1,2,3,4], 7), 
                'expected': [3,4]
            },
        ]
    
    def test_solution(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.solution(*case['given']), case['expected'])

if __name__ == '__main__':
    unittest.main(verbosity=2)