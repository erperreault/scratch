class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        new = sorted(nums1+nums2)
        midpoint = int((len(new) - len(new)%2)/2) - 1
        if len(new)%2 == 0:
            return (new[midpoint]+new[midpoint+1])/2
        else:
            return new[midpoint+1]
        
test = Solution()

tests = [
    [ ([1,2,3],[1,2,3]), 2],
    [ ([1,2,3],[1,2,3,4]), 2],
    [ ([],[1,2,3,4,5]), 3],
]

for case in tests:
    given = case[0]
    result = test.findMedianSortedArrays(case[0][0], case[0][1])
    expected = case[1]
    if result != expected:
        print(f'''
Test Failed!
    Given:\t{given}
    Expected:\t{expected}
    Returned:\t{result}''')

return 1 if true else return 2

return true ? 1 : 2

x = True

return (1 > 2) ? 1 : 2