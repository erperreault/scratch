class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        if len(dominoes) < 2:
            return dominoes

        d = list(dominoes)
        
        while True:
            new = d[:]
            if d[0] == '.' and d[1] == 'L':
                new[0] = 'L'
            if d[-1] == '.' and d[-2] == 'R':
                new[-1] = 'R'

            for i in range(1, len(d)-1):
                if d[i] == '.':
                    if d[i+1] == 'L' and d[i-1] != 'R':
                        new[i] = 'L'
            for i in range(len(d)-2, 0, -1):
                if d[i] == '.':
                    if d[i+1] != 'L' and d[i-1] == 'R':
                        new[i] = 'R'

            if new == d:
                return ''.join(d)
            else:
                d = new[:]

test = Solution()

tests = [
    ['.L.R...LR..L..', 'LL.RR.LLRRLL..'],
    ['RR.L', 'RR.L'],
    ['..R..', '..RRR'],
    ['.....', '.....'],
    ['.', '.'],
    ['RRR', 'RRR'],
    ['R.R', 'RRR'],
    ['...L', 'LLLL'],
    ['.R.L', '.R.L'],
    ['.L', 'LL'],
    ['..L', 'LLL'],
    ['..........L', 'LLLLLLLLLLL'],
]

for case in tests:
    given = case[0]
    result = test.pushDominoes(case[0])
    expected = case[1]
    if result != expected:
        print(f'''
Test Failed!
    Given:\t{given}
    Expected:\t{expected}
    Returned:\t{result}''')