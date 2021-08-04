from test import data

def solution_a(data):
    d = data.split('\n\n')
    invalid = 0
    fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ]
    for ps in d:
        for field in fields:
            if field not in ps:
                invalid += 1
                break
            
    return len(d) - invalid

def solution_b(data):
    pass

print(solution_a(data))
print(solution_b(data))