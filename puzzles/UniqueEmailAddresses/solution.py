# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/639/week-4-september-22nd-september-28th/3989/

class Solution:

    def solution(self, emails: list) -> int:
        unique = []
        
        for e in emails:
            e = e.split('@')
            if '+' in e[0]:
                e[0] = e[0].split('+')[0]
            if '.' in e[0]:
                e[0] = ''.join(e[0].split('.'))
            e = '@'.join(e)
            unique.append(e)
            
        return len(set(unique))