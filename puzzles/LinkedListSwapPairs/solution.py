class Solution:
    def solution(self, head):
        current = head
        
        if current:
            while current.next:
                temp = current.val
                current.val = current.next.val
                current.next.val = temp
                if current.next.next:
                    current = current.next.next
                else:
                    break
                
        return head