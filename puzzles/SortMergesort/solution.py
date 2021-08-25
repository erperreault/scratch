class Solution:

    def solution(self, a: list) -> list:
        mid = len(a) // 2

        a1 = self.solution(a[:mid])
        a2 = self.solution(a[mid:])

        return self.merge(a1, a2)

    def merge(self, a1: list, a2: list) -> list:
        result = []
        i = 0
        j = 0

        while i < len(a1) and j < len(a2):
            if a1[i] < a2[j]:
                result.append(a1[i])
                i += 1
            else:
                result.append(a2[j])
                j += 1
        
        result += a1[i:]
        result += a2[j:]

        return result