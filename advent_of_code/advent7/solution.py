from test import data

def solution_a(data):
    splitted = data.split('\n')
    pre_keys = [ r.split('contain')[0].strip() for r in splitted ]
    keys = [ ' '.join(r.split()[:2]) for r in pre_keys ]
    pre_vals = [ r.split('contain')[1].strip() for r in splitted ]
    vals = [ ' '.join(r.split()[1:3]) for r in pre_vals ]
    x = dict(zip(keys, vals))
    queue = ['shiny gold']
    ans = []


    #this is currently only catching the first color under the contents for
    # each bag, thanks to careless splitting
    while queue:
        test = queue.pop(0)
        for container in keys:
            print(f'{container=}, {x[container]=}')
            if test in x[container]:
                new = ' '.join(container.split()[:2])
                print(f'{new=}')
                queue.append(new)
                ans.append(new)

    return len(set(ans))

def solution_b(data):
    pass

print(solution_a(data))
print(solution_b(data))