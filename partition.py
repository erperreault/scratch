class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        for i in range(1, len(nums)-1):
            if max(nums[:i]) <= min(nums[i:]):
                return i
        
        return len(nums) - 1


test = Solution()

tests = [
    ( [5,0,3,8,6], 3 ),
    ( [1,1], 1 ),
    ( [90,47,69,10,43,92,31,73,61,97], 9 ),
]

for case in tests:
    given = case[0]
    result = test.partitionDisjoint(case[0])
    expected = case[1]
    if result != expected:
        print(f'''
Test Failed!
    Given:\t{given}
    Expected:\t{expected}
    Returned:\t{result}''')