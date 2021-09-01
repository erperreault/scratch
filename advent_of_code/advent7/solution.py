from test import data
import re

def solution_a(data):
    lines = data.split('\n')
    color_re = re.compile('([\D]*)bag')
    colors = [ color_re.findall(line) for line in lines ]
    outer = [ color[0].strip() for color in colors ]
    inner = [ color[1:] for color in colors ]
    clean = []
    for line in inner:
        clean.append([ color.strip() for color in line ])
    d = dict(zip(outer,clean))

    final = []

    queue = ['shiny gold']
    while queue:
        for i in range(len(queue)):
            current = queue.pop()
            for color in d.keys():
                if current in d[color]:
                    final.append(color)
                    queue.append(color)

    return len(set(final))

def solution_b(data):
    lines = data.split('\n')

    color_re = re.compile('([\D]*)bag')
    colors = [ color_re.findall(line) for line in lines ]
    outer = [ color[0].strip() for color in colors ]
    inner = [ color[1:] for color in colors ]
    clean = []
    for line in inner:
        clean.append([ color.strip() for color in line ])    
    color_dict = dict(zip(outer,clean)) 
        
    number_re = re.compile('\d')
    numbers = [ number_re.findall(line) for line in lines ]
    ints = []
    for line in numbers:
        ints.append([ int(i) for i in line ])
    number_dict = dict(zip(outer, ints))

    ans = 0
    queue = ['shiny gold']

    while queue:
        current = queue.pop()
        if current in number_dict.keys():
            ans += sum(number_dict[current])
            for color in color_dict[current]:
                queue.append(color)

    return ans

# print(solution_a(data))
print(solution_b(data))
# 447 too low