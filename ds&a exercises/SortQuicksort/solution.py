class Solution:

    def solution(self, a, low=0, high=None):
        if high is None:
            high = len(a) - 1

        if high - low < 2:
            return a

        pivot = self.partition(a, low, high)

        self.solution(a, 0, pivot)
        self.solution(a, pivot+1, high)

        return a

    def partition(self, a, start, end):
        pivot = start
        i = start
        j = start + 1

        while j < end:
            if a[j] < pivot:
                i += 1
                a[j], a[i] = a[i], a[j]
            j += 1
        
        a[i], a[pivot] = a[pivot], a[i]

        return i