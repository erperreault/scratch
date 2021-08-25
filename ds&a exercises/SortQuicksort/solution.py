class Solution:

    def solution(self, a: list) -> list:
        pivot = len(a)-1
        i = 0
        j = 1

        while a[i] < a[pivot]:
            