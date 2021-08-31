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
    pass

print(solution_a(data))