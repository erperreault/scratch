# https://www.codewars.com/kata/5b3077019212cbf803000057/train/python

mode_1 = [
    list('abcde123'),
    list('fghij456'),
    list('klmno789'),
    list('pqrst.@0'),
    list('uvwxyz_/'),
    'aA# SP'.split(' '),
]

mode_2 = [
    list('ABCDE123'),
    list('FGHIJ456'),
    list('KLMNO789'),
    list('PQRST.@0'),
    list('UVWXYZ_/'),
    'aA# SP'.split(' '),
]

mode_3 = [
    list('^~?!'"()"),
    list('-:;+&%*='),
    list('<>€£$¥¤\\'),
    list('[]{},.@§'),
    list('#¿¡_/'),
    'aA# SP'.split(' '),
]

modes = {
    'mode_1': mode_1,
    'mode_2': mode_2,
    'mode_3': mode_3,
}

def tv_remote(words):
    coords = [0, 0]
    keyboard = mode_1
    keypresses = 0
    targets = list(words)
    print(f'{targets=}')

    return keypresses

def target_mode(character):
    for line in mode_1:
        if character in line:
            return 'mode_1'
    for line in mode_2:
        if character in line:
            return 'mode_2'
    for line in mode_3:
        if character in line:
            return 'mode_3'

print(f"{target_mode('c')=}")
print(f"{target_mode('Z')=}")
print(f"{target_mode('$')=}")
print(target_mode('\\'))
print(f"{tv_remote('hello world')=}")