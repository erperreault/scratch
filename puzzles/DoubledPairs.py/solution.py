class Solution:
    """Given an array of integers arr of even length, return true if and only if 
    it is possible to reorder it such that arr[2 * i + 1] = 2 * arr[2 * i] for 
    every 0 <= i < len(arr) / 2.
    
    Re-ordering doesn't actually matter
    Find lowest member, check if double is in list. If so remove both.
    This should allow for logN time complexity"""
    
    def solution(self, arr):
        """Sort the list once to save time finding lowest member each pass."""
        arr.sort()
        
        while arr:
            """Pop lowest, look for double and remove if found."""
            x = arr.pop(0)
            
            """Work in one direction instead of pivoting at 0."""
            if x >= 0:
                y = 2 * x
            else:
                y = .5 * x
            
            """Removing each pair lets us run in logN time."""
            if y in arr:
                arr.remove(y)
            else:
                return False
        
        return True

test = Solution()
cases = [
    { 
    'given': [1,2,4,16,8,4], 
    'expected': False
    }, {
    'given': [3,1,3,6],
    'expected': False
    }, {
    'given': [4,-2,2,-4],
    'expected': False 
    },
]

for case in cases:
    print(f"{test.solution(case['given'])=} (expected {case['expected']})")