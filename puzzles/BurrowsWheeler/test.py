import unittest
from solution import Solution as target

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            { 
                'original':    'bananabar', 
                'encoded':     ['nnbbraaaa', 4]
            },
            { 
                'original':    'Humble Bundle', 
                'encoded':     ['e emnllbduuHB', 2]
            },
            { 
                'original':    'Mellow Yellow', 
                'encoded':     ['ww MYeelllloo', 1]
            },
        ]
    
    def test_encode(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.encode(case['original']), case['encoded'])
    
    def test_decode(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.decode(*case['encoded']), case['original'])

if __name__ == '__main__':
    unittest.main(verbosity=2)