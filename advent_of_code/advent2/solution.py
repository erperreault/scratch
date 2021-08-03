from test import data

def solution_a(data):
    d = [ [i.split(':')[0].split(), i.split(':')[1]] for i in data.split('\n')]
    ans = 0

    for i in d:
        policy_min = int(i[0][0].split('-')[0])
        policy_max = int(i[0][0].split('-')[1])
        policy_letter = i[0][1]
        password = i[1]
        
        if policy_min <= password.count(policy_letter) <= policy_max:
            ans += 1

    return ans

def solution_b(data):
    d = [ [i.split(':')[0].split(), i.split(':')[1]] for i in data.split('\n')]
    ans = 0

    for i in d:
        slot_a = int(i[0][0].split('-')[0])
        slot_b = int(i[0][0].split('-')[1])
        policy_letter = i[0][1]
        password = i[1]
        print([password[slot_a], password[slot_b]], f'{policy_letter=}, {password=}')
        
        if [password[slot_a], password[slot_b]].count(policy_letter) == 1:
            ans += 1

    return ans


print(solution_b(data))