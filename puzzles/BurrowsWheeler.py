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
        """
        this is the fancy trick: you can rebuild the original by tacking the encoded string onto
        the fronts of each row and sorting alphabetically each time. answer is at the same index
        after completing the table. table could be skipped by just sorting what you have and
        checking the index each time.
        """
        table = sorted([s[i] for i in range(len(s))])
        for x in range(len(s)-1):
            for y in range(len(s)):
                table[y] = s[y] + table[y]
            table.sort()
        
        return table[i]