from test import data

def solution_a(data):
    d = data.split()
    coords = [0,0]
    trees = 0

    while coords[0] < len(d)-1:
        coords[0] += 1
        coords[1] = (coords[1] + 3) % len(d[0])
        if d[coords[0]][coords[1]] == '#':
            trees += 1

    return trees

def solution_b(data):
    return 0


print(solution_a(data))
print(solution_b(data))