# for https://www.codewars.com/kata/52cf02cd825aef67070008fa/train/python

def decode(s):
    print('custom test cases:')
    print('\t' + str(ord(encode('a')))) # unicode a is 97, yields 98
    print('\t' + to_ord(encode('ab'))) # yields 98, 104
    print('\t' + to_ord(encode('abcdefghijklmnopqrstuvwxyz'))) # yields 98, 104, 120, 44, 122, 87, 121, 76, 90
    for c in "abcdefghijklmnopqrstuvwxyz":
        print('\t' + to_ord(encode(c))) # wraps around at 122 -> 66
    print([int(to_ord(c)) for c in encode("abcdefghijklmnopqrstuvwxyz")])
        
    alphabet = [to_ord(c) for c in encode('abcdefghijklmnopqrstuvwxyz')]
    diffs = []
    for c in range(len(alphabet)-1):
        diffs.append(int(alphabet[c+1]) - int(alphabet[c]))
    print(diffs)
        
    alphabet = [to_ord(c) for c in encode(reversed('abcdefghijklmnopqrstuvwxyz'))]
    diffs = []
    for c in range(len(alphabet)-1):
        diffs.append(int(alphabet[c+1]) - int(alphabet[c]))
    print(diffs)
        
    print(encode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    print(encode("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))
    print(encode("!@#$%^&*()_+-"))
    a,b,c = "", "", ""
    for w in "abcdefghijklmnopqrstuvwxyz":
        a += encode(  "" + w)[0]
        b += encode( "_" + w)[1]
        c += encode("__" + w)[2]
    print(a)
    print(b)
    print(c)
    return s;

def to_ord(s):
    return ''.join([f'{ord(i)}' for i in s])