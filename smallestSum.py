"""
https://www.codewars.com/kata/52f677797c461daaf7000740/train/python

Given an array lowest_value of positive integers, its elements are to be transformed by running 
the following operation on them as many times as required:

if X[i] > X[j] then X[i] = X[i] - X[j]

When no more transformations are possible, return its sum ("smallest possible sum").
"""

def solution(array):
    lowest = array.pop()
    count = 1

    while array:
        current = array.pop()
        count += 1
        if lowest > 1:
            remainder = max(current, lowest) % min(current, lowest)
            if remainder:
                lowest = remainder
            else:
                lowest = min(current, lowest)

    return lowest * count

test = [3, 13, 23, 7, 83]
print(solution(test) == 5)

test = [1,21,55]
print(solution(test) == 3)

test = [1,2,3,4,5,6,7,8,9]
print(solution(test) == 9)

test = [9]
print(solution(test) == 9)

test = [6,9,21]
print(solution(test) == 9)