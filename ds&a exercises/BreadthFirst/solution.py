"""Implement breadth-first search on a binary tree.
Variant: return the level-order traversal of the full tree as an array of arrays.
"""

class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def populate_tree(self, max: int) -> Node:
        self.tree = Node(0)
        current = self.tree
        for i in range(max):

            current = self.left

    def solution(self, max, target):
        tree = self.populate_tree(max)

        return 0