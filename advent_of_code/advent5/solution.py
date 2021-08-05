from test import data

def solution_a(data):
    d = data.split()
    highest = 0

    for seat in d:
        print(seat)
        col = [0,8]
        row = [0,128]
        for letter in seat:
            if letter == 'F':
                row[1] -= (row[1] - row[0]) / 2
            elif letter == 'B':
                row[0] += (row[1] - row[0]) / 2
            elif letter == 'L':
                col[1] -= (col[1] - col[0]) / 2
            elif letter == 'R':
                col[0] += (col[1] - col[0]) / 2
        
        print(f'{row=}, {col=}')
        row[1] -= 1
        col[1] -= 1
        print(f'{row=}, {col=}')
        
        seat_num = int(row[1]*8 + col[1])
        if seat_num > highest:
            highest = seat_num

    return highest

def solution_b(data):
    pass

print(solution_a(data))
print(solution_b(data))