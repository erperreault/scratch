import unittest

def valid_solution(board): #board[i][j]
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

class TestSudokuChecker(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(valid_solution(test_cases['first']), True)
        self.assertEqual(valid_solution(test_cases['second']), False)

test_cases = {
    'first':   [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                [6, 7, 2, 1, 9, 5, 3, 4, 8],
                [1, 9, 8, 3, 4, 2, 5, 6, 7],
                [8, 5, 9, 7, 6, 1, 4, 2, 3],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 6, 1, 5, 3, 7, 2, 8, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 4, 5, 2, 8, 6, 1, 7, 9]],

    'second':  [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
                [6, 7, 2, 1, 9, 0, 3, 4, 9],
                [1, 0, 0, 3, 4, 2, 5, 6, 0],
                [8, 5, 9, 7, 6, 1, 0, 2, 0],
                [4, 2, 6, 8, 5, 3, 7, 9, 1],
                [7, 1, 3, 9, 2, 4, 8, 5, 6],
                [9, 0, 1, 5, 3, 7, 2, 1, 4],
                [2, 8, 7, 4, 1, 9, 6, 3, 5],
                [3, 0, 0, 4, 8, 1, 1, 7, 9]],
}

if __name__ == '__main__':
    unittest.main()