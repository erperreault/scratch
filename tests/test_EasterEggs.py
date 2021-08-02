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
        ]

        """
            { 
                'given':    [7, 500], 
                'expected': 1507386560013475 
            },
            { 
                'given':    [237, 500], 
                'expected': 431322842186730691997112653891062105065260343258332219390917925258990318721206767477889789852729810256244129132212314387344900067338552484172804802659 
            },
            { 
                'given':    [477, 500], 
                'expected': 3273390607896141870013189696827599152216642046043064789483291368096133796404674554883270092325904157150886684127420959866658939578436425342102468327399 
            },"""
    
    def test_solution(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.solution(*case['given']), case['expected'])

if __name__ == '__main__':
    unittest.main(verbosity=2)