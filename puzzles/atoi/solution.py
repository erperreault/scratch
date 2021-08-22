class Solution:
    def solution(self, s: str) -> int:
        if not s:
            return 0
        
        ptr = 0
        total = 0
        sign = 1
        
        while s[ptr] == ' ':
            ptr += 1
            if ptr == len(s):
                return 0
            
        if s[ptr] == '+':
            ptr += 1
        elif s[ptr] == '-':
            sign = -1
            ptr += 1
            
        if ptr == len(s):
            return 0
            
        while ptr < len(s):
            if s[ptr].isnumeric():
                total *= 10
                total += int(s[ptr])
                ptr += 1
            else:
                break
        
        total *= sign
        
        if total > 2147483647:
            return 2147483647
        elif total < -2147483648:
            return -2147483648
        else:
            return total