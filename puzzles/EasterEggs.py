"""
https://www.codewars.com/kata/54cb771c9b30e8b5250011d4/train/python

you should calculate maximum scyscrapper height (in floors), in which it is 
guaranteed to find an exactly maximal floor from which that an egg won't crack it.

so, given x eggs and y tries, what's the max height we can find a safe floor for?
0 eggs -> 0 height safely checked
0 tries -> 0 height safely checked

2 eggs, 14 tries -> 105 (why is this?)
105 = 14+13+12+...+1
so once we break our first egg, we can use the other for the amount of tries remaining to test floors
if we have 3 eggs, does that simply double the answer? test at 210 and then at 105?

given eggs == tries:
1 -> 1
2 -> 3 (test at 2, test remainder)
3 -> 7 (test at 4, test 123/567, test remainder)
4 -> 15 (test at 8, 4, 2, 1) or (8, 12, 14, 15)
n -> (2^n) - 1
window is min of eggs,tries. max is tries * window
"""

class Solution:
    def solution(self, eggs, tries):
        if eggs == 0 or tries == 0:
            return 0

        if tries == 1:
            return 1
        
        if eggs == 1:
            return tries

        return sum([1, self.solution(eggs-1, tries-1), self.solution(eggs, tries-1)])