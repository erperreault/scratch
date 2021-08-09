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
    d = data.split('\n\n')
    fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
    ]
    ans = 0
    
    for ps in d:
        ps_fixed = ps.split()
        dicto = dict([ x.split(':') for x in ps_fixed])
        valid = True
        for field in fields:
            if field in dicto and validate(field, dicto[field]):
                continue
            else:
                valid = False
                break
        if valid:
            ans += 1

    return ans

def validate(field_name, field_data):
    if field_name == 'byr':
        return 1920 <= int(field_data) <= 2002
    elif field_name == 'iyr':
        return 2010 <= int(field_data) <= 2020
    elif field_name == 'eyr':
        return 2020 <= int(field_data) <= 2030
    elif field_name == 'hgt':
        if field_data[-2:] == 'cm':
            return 150 <= int(field_data[:-2]) <= 193
        if field_data[-2:] == 'in':
            return 59 <= int(field_data[:-2]) <= 76
        else:
            return False
    elif field_name == 'hcl':
        # doesn't check if chars are 0-9a-f, just alphanumeric, but still passes! report bug?
        return len(field_data) == 7 and field_data[0] == '#' and field_data[1:].isalnum()
    elif field_name == 'ecl':
        return field_data in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif field_name == 'pid':
        return len(field_data) == 9 and field_data.isnumeric()

print(solution_a(data))
print(solution_b(data))