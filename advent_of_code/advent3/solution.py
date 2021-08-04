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
    d = data.split()

    ans = 1

    slopes = [
        [1,1], # [x,y]
        [3,1],
        [5,1],
        [7,1],
        [1,2],
    ]

    for slope in slopes:
        trees = 0
        coords = [0,0]

        while coords[0] < len(d)-1:
            coords[0] += slope[1] # y change
            coords[1] = (coords[1] + slope[0]) % len(d[0]) # x change and wrap
            if d[coords[0]][coords[1]] == '#':
                trees += 1

        ans *= trees
    return ans


print(solution_a(data))
print(solution_b(data))