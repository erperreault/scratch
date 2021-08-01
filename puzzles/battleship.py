# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python

def validate_battlefield(field):
    """
    first: check that no ships are overlapping -
    this can be done by counting the total number of 1s
    """
    
    total_squares = sum([sum(row) for row in field])
    print(f'total squares = {total_squares} (expected 20)')
    
    """
    next: check that correct roster of ships are present
    scanning L->R, top->bot will always find the first cell of a ship, 
    then either scan ->R or ->bot. for each 1, find east/south neighboring 1 
    and set direction. continue checking in that direction until end,
    increment appropriate ship count & store its coordinates to be ignored later
    """

    x = 0
    y = 0

    seen = []
    ships = []

    for y in range(len(field)):
        for x in range(len(field[y])):
            if [x,y] not in seen and field[y][x] == 1:
                seen.append([x,y])
                scan = [x,y]
                ship_length = 1

                while scan[0] < len(field[y]) - 1 and field[scan[1]][scan[0]+1] == 1:
                    # scan east
                    scan = [scan[0]+1,scan[1]]
                    ship_length += 1
                    seen.append(scan)
                while scan[1] < len(field) - 1 and field[scan[1]+1][scan[0]] == 1:
                    # scan south
                    scan = [scan[0],scan[1]+1]
                    seen.append(scan)
                    ship_length += 1
                ships.append(ship_length)
    print(ships)

    # check ship roster
    if sorted(ships) != [1,1,1,1,2,2,2,3,3,4]:
        return False
    
    """
    note: ships may not be in contact by edge or corner!
    only need to check four corners.
    this will take care of edge contact as well, because ships longer than 1
    always include a diagonal if in contact, and 1-length ships will look like 
    a larger ship of invalid length
    """
    
    for coords in seen:
        for neighbor in [ [-1,-1], [-1,1], [1,-1], [1,1] ]:
            if [ coords[0]+neighbor[0], coords[1]+neighbor[1] ] in seen:
                return False

    return True

battleField = [
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

print(validate_battlefield(battleField))