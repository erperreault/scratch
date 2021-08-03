from test import data

def solution(data):
    d = [int(x) for x in data]
    while d:
        i = d.pop(0)
        first_diff = 2020 - i

        for j in d:
            second_diff = first_diff - j
            if second_diff in d:
                return i * second_diff * j

