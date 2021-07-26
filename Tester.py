class Tester:
    def __init__(self, tests: list, target: function):
        self.tests = tests
        self.target = target

    def run_tests(self):
        for case in self.tests:
            given = case[0]
            result = self.target(case[0])
            expected = case[1]
            
            if result != expected:
                print(f'''
        Test Failed!
            Given:\t{given}
            Expected:\t{expected}
            Returned:\t{result}''')