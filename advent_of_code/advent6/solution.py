from test import data

def solution_a(data):
    """Harder to read one-liner."""
    #return sum([ len(set(group.replace('\n', ''))) for group in data.split('\n\n') ])

    formatted = [ group.replace('\n', '') for group in data.split('\n\n') ]
    return sum([ len(set(group)) for group in formatted ])

def solution_b(data):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    formatted = [ group.split('\n') for group in data.split('\n\n') ]
    ans = 0

    """Check that a letter is present in all members of a group."""
    def check_group(group: list, letter: str):
        for person in group:
            if letter not in person:
                return False
        
        return True

    for group in formatted:
        total = 0
        for letter in alphabet:
            if check_group(group, letter):
                total += 1
        
        ans += total
                    
    return ans

#print(solution_a(data))
print(solution_b(data))