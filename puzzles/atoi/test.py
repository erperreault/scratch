import unittest
from solution import Solution as target

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            { 
                'given':    "42", 
                'expected': 42
            },
            { 
                'given':    "   -42", 
                'expected': -42
            },
            { 
                'given':    "4193 with words", 
                'expected': 4193
            },
            { 
                'given':    "words and 987", 
                'expected': 0
            },
            { 
                'given':    "-91283472332", 
                'expected': -2147483648
            },
            { 
                'given':    "", 
                'expected': 0
            },
            { 
                'given':    " ", 
                'expected': 0
            },
        ]
    
    def test_solution(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.solution(case['given']), case['expected'])

if __name__ == '__main__':
    unittest.main(verbosity=2)