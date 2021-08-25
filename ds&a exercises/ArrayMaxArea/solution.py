class Solution:
    def solution(self, height: list[int]) -> int:
        ans = 0
        
        l = 0
        r = len(height)-1
        
        while l < r:
            area = (r-l)*(min(height[r],height[l]))
            if area > ans:
                ans = area
                
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return ans