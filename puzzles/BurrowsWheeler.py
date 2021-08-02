class Solution:
    def encode(self, s):
        table = []
        for i in range(len(s)):
            table.append(s)
            s = s[-1] + s[:-1]
        table.sort()
        t = ''.join([c[-1] for c in table])
        i = table.index(s)
        return [t, i]

    def decode(self, s, i):
        table = sorted([s[i] for i in range(len(s))])
        for x in range(len(s)-1):
            for y in range(len(s)):
                table[y] = s[y] + table[y]
            table.sort()
        
        return table[i]