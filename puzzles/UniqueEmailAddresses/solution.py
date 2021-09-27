# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/639/week-4-september-22nd-september-28th/3989/

class Solution:

    def solution(self, emails: list) -> int:
        unique = []

        for e in emails:
            if '@' not in e or '.' not in e:
                continue
            e = e.split('@')
            if len(e) != 2 or '.' not in e[1]:
                continue
            if '+' in e[0]:
                e[0] = e[0].split('+')[0]
            if '.' in e[0]:
                e[0] = ''.join(e[0].split('.'))
            e = ''.join(e)
            print(e)
            if e in unique:
                continue
            unique.append(e)


        return len(unique)