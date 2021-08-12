class Solution:

    def solution(self):
        return 0

cases = [
    { 
    'given':    0, 
    'expected': 0
    },
]

for case in cases:
    test = Solution()
    try:
        assert(test.solution(case['given']) == case['expected'])
    except AssertionError:
        print(f"{case['given']} Test Failed")