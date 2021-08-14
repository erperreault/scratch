import unittest
from solution import Solution as target

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            { 
                'given':    [5,2,3,1], 
                'expected': [1,2,3,5]
            },
        ]
    
    def test_solution(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.sortArray(case['given']), case['expected'])

if __name__ == '__main__':
    unittest.main(verbosity=2)