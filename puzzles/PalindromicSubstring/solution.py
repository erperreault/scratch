class Solution:
    def solution(self, s: str) -> str:
        head = 2
        tail = 0
        
        if len(s) > 0:
            self.best = s[0]
        else:
            return ''
        
        while head <= len(s):
            if s[head-1] == s[tail]:
                self.check_palindrome(s, head, tail)
                
            head += 1
            
            if head > len(s):
                break
                
            if s[head-1] == s[tail]:
                self.check_palindrome(s, head, tail)
                
            tail += 1
            
        return self.best
                
    def check_palindrome(self, s, head, tail):
        h = head
        t = tail
        if h - t > len(self.best):
            self.best = s[t:h]
            
        while h <= len(s) and t >= 0 and s[h-1] == s[t]:
            if h - t > len(self.best):
                self.best = s[t:h]
            h += 1
            t -= 1