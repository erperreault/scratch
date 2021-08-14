class Node:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

class Solution:
    """Implement a linked list."""

    def solution(self, start: int):
        head = Node(val=start)
        current = head
        ans = []

        """Populate a list with new nodes of decreasing value."""
        while current.val >= 0:
            current.next = Node(val=current.val-1)
            current = current.next

        """Start from the head node and read values until final node."""
        new = head
        while new.next is not None:
            ans.append(new.val)
            new = new.next

        return ans