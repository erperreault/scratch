from test import data

def solution_a(data):
    d = data.split()
    highest = 0

    for seat in d:
        col = 7
        col_step = 4
        row = 127
        row_step = 64

        for letter in seat[:7]:
            if letter == 'F':
                row -= row_step
            row_step /= 2

        for letter in seat[7:]:
            if letter == 'L':
                col -= col_step
            col_step /= 2
        
        seat_num = int(row*8 + col)
        if seat_num > highest:
            highest = seat_num

    return highest

def solution_b(data):
    d = data.split()
    seats = []

    for seat in d:
        col = 7
        col_step = 4
        row = 127
        row_step = 64

        for letter in seat[:7]:
            if letter == 'F':
                row -= row_step
            row_step /= 2

        for letter in seat[7:]:
            if letter == 'L':
                col -= col_step
            col_step /= 2
        
        seat_num = int(row*8 + col)
        seats.append(seat_num)

    for i in range(max(seats)):
        if i not in seats and i+1 in seats and i-1 in seats:
            return i

print(solution_a(data))
print(solution_b(data))