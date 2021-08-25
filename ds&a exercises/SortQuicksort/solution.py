class Solution:

    def solution(self, a: list) -> list:
        """This solution does not sort in place but is very easy to understand."""
        if len(a) < 2:
            return a

        less, equal, greater = [], [], []
        pivot = a[0]

        for i in a:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)
            
        return self.solution(less) + equal + self.solution(greater)