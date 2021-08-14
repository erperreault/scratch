"""Implement a linked list.
Define a Node class, and populate a linked list of Nodes with values counting up from
the given positive start integer until double its value (exclusive).

Write a second method, which reads the values of the linked list and returns them as an array.

Integers less than 1 should return an empty array.
"""

class Node:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

class Solution:
    def solution(self, start: int):
        head = self.populateList(start)
        return self.traverseList(head)

    def populateList(self, start) -> Node:
        head = Node(val=start)
        current = head

        while current.val < start*2:
            current.next = Node(val=current.val+1)
            current = current.next

        return head

    def traverseList(self, head: Node) -> list:
        output = []
        current = head

        while current.next is not None:
            output.append(current.val)
            current = current.next

        return output