import unittest
from solution import Solution as target

class TestSomething(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            { 
                'given':    ['mysite.com/pictures/holidays.html', ' : '], 
                'expected': '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
            },
            { 
                'given':    ['www.codewars.com/users/GiacomoSorbi?ref=CodeWars', ' / '], 
                'expected': '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
            },
            { 
                'given':    ['www.microsoft.com/important/confidential/docs/index.htm#top', ' * '], 
                'expected': '<a href="/">HOME</a> * <a href="/important/">IMPORTANT</a> * <a href="/important/confidential/">CONFIDENTIAL</a> * <span class="active">DOCS</span>'
            },
            { 
                'given':    ['mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp', ' > '], 
                'expected': '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
            },
            { 
                'given':    ['www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi', ' + '], 
                'expected': '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'
            },
            { 
                'given':    ['https://www.linkedin.com/in/giacomosorbi', ' * '], 
                'expected': '<a href="/">HOME</a> * <a href="/in/">IN</a> * <span class="active">GIACOMOSORBI</span>'
            }
        ]
    
    def test_solution(self):
        for case in self.test_cases:
            test = target()
            self.assertEqual(test.solution(*case['given']), case['expected'])

if __name__ == '__main__':
    unittest.main(verbosity=2)