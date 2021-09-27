import unittest
from solution import Solution as target

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            {
                'given':    ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"], 
                'expected': 2 
            },
            {
                'given':    ["a@leetcode.com","b@leetcode.com","c@leetcode.com"], 
                'expected': 3 
            }, 
        ]
    
    def test_solution(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.solution(case['given']), case['expected'])

if __name__ == '__main__':
    unittest.main(verbosity=2)