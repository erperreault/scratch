from test import data

def solution_a(data):
    """Harder to read one-liner."""
    #return sum([ len(set(''.join(x.split('\n')))) for x in data.split('\n\n') ])

    formatted = [ ''.join(group.split('\n')) for group in data.split('\n\n') ]
    return sum([ len(set(group)) for group in formatted ])

def solution_b(data):
    pass

print(solution_a(data))
#print(solution_b(data))