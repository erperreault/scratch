class Solution:
    """https://leetcode.com/problems/zigzag-conversion/"""
    def solution(self, source: str, rows: int) -> str:
        if rows == 1:
            return source
        
        ans = [''] * rows    
        current_row = 0

        for c in source:
            ans[current_row] += c

            if current_row == 0:
                walk_direction = 1
            elif current_row == rows-1:
                walk_direction = -1
            
            current_row += walk_direction

        return ''.join(ans)