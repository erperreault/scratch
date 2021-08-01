"""
Given an array nums of n integers and an integer target, 
find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. 
You may assume that each input would have exactly one solution.
"""

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        ans_diff = 100000

        for i in range(len(nums)-2):
            a = nums[i]
            for j in range(i+1, len(nums)-1):
                b = nums[j]
                for k in range(j+1, len(nums)):
                    c = nums[k]
                    sum = a+b+c
                    
                    if (target > 0 and sum > 0) or (target < 0 and sum < 0):
                        diff = abs(sum - target)
                    else:
                        diff = max(sum, target) - min(sum, target)
                    print(a, b, c, '-> sum =', a+b+c, ', diff = ', diff)
                        
                    if diff < ans_diff:
                        ans = sum
                        ans_diff = diff

        return ans
        
test = Solution()
print(f'{test.threeSumClosest(nums=[-1,2,1,-4], target = 1)}')
print(f'{test.threeSumClosest(nums=[1,1,1,0], target = -100)}')