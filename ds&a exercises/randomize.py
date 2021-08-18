import random

exercises = {
    'Linked List':  '''Implement a linked list.
Define a Node class, and populate a linked list of Nodes. 
Write a second method, which reads the values of the linked list and returns them as an array.''',
    'Breadth First':  '''Implement breadth-first search on a binary tree.
Variant: return the level-order traversal of the full tree as an array of arrays.''',
    'Depth First':  '''Implement depth-first search on a binary tree.
Variant: return the in-order traversal of the full tree as an array of arrays.''',
    'Merge Sort':   '''Implement merge sort on an array of integers.
Variant: implement alphabetical merge sort on an array of strings''',
    'Binary Search': '''Implement binary search of a sorted array of integers.
Return the index of the target integer if it is present, or else -1 if it is absent.
Variant: use binary search to find the first number greater than a cutoff value (given as 'target').''',
    'Binary Tree': '''Implement a binary tree data structure. Given an array (with nulls for non-existent nodes), populate the tree.''',
    'Balanced Binary Tree': '''Given a binary tree, determine if it is balanced.''',
}


if __name__ == '__main__':
    selection = random.choice(list(exercises.keys()))
    print('//////////\n')
    print(f'{selection}\n\n{exercises[selection]}')
    print('\n//////////')