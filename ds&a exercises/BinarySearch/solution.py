"""Implement binary search of a sorted array of integers.
Return the index of the target integer if it is present, or else -1 if it is absent.

Variant: 
Use binary search to find the first number greater than a cutoff value (given as 'target').
"""

class Solution:
    """Solve for base case."""
    def solution(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = (low + high)//2
            
            if nums[mid] == target:
                return mid
            
            else:
                if nums[mid] < target:
                    low = mid + 1
                if nums[mid] > target:
                    high = mid - 1
                    
        return -1

    """Variant solution."""
    def v_solution(self):
        pass