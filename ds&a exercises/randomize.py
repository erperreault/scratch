import random

exercises = {
    'Linked List':  '''Implement a linked list.
Define a Node class, and populate a linked list of Nodes with values counting up from
the given positive start integer until double its value (exclusive).

Write a second method, which reads the values of the linked list and returns them as an array.

Integers less than 1 should return an empty array.''',
    'Linked List':  '''Implement a linked list.
Define a Node class, and populate a linked list of Nodes with values counting up from
the given positive start integer until double its value (exclusive).

Write a second method, which reads the values of the linked list and returns them as an array.

Integers less than 1 should return an empty array.''',
}


if __name__ == '__main__':
    selection = random.choice(list(exercises.keys()))
    print(f'\n{selection}\n\n{exercises[selection]}\n')