class Solution:
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