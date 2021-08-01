class SudokuChecker:
    def solution(board): #board[i][j]
        size = 9
        subSize = 3
        correct = list(range(1, size+1))
        
        for row in board:
            if sorted(row) != correct:
                return False
            
        for column in zip(*board): # review and memorize this handy trick
            if sorted(column) != correct:
                return False 
            
        for x in range(0, size, subSize): # if subSize 3: 0, 4, 7, ...
            for y in range(0, size, subSize):
                region = []
                for a in range(x, x + subSize):
                    for b in range(y, y + subSize):
                        region.append(board[a][b])
                if sorted(region) != correct:
                    return False 
                
        return True