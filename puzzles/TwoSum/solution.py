class Solution:
    def solution(self, nums: list[int], target: int) -> list[int]:
        """Naive/brute force approach."""
        for i in range(0, len(nums)-1):
            test = target - nums[i]
            
            for j in range(i+1, len(nums)):
                if nums[j] == test:
                    return [i,j]