class Solution:
    def solution(self, nums: list[int]) -> int:
        ans = 0
        visited = set()
        for i in nums:
            if i not in visited: # duplicates represent a loop, so skip all visited
                s = set()
                x = 0
                while i not in s:
                    s.add(i)
                    visited.add(i)
                    i = nums[i]
                    x += 1
                if x > ans:
                    ans = x
                
        return ans