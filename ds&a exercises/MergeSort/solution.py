"""Implement merge sort on an array of integers.
Variant: implement alphabetical merge sort on an array of strings."""

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        length = len(nums)
        
        if length == 1:
            return nums
        
        partition = length//2
        
        a1 = self.sortArray(nums[:partition])
        a2 = self.sortArray(nums[partition:])
        
        return self.merge(a1, a2)
    
    def merge(self, a1, a2):
        new = []
        i = j = 0
        
        while i < len(a1) and j < len(a2):
            if a1[i] < a2[j]:
                new.append(a1[i])
                i += 1
            else:
                new.append(a2[j])
                j += 1
                
        new.extend(a1[i:])
        new.extend(a2[j:])
            
        return new