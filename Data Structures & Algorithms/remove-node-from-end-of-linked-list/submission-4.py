# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current is not None:
            current = current.next
            length += 1
        
        index = length - n
        i = 0
        current = head
        prev = None
        while i < index:
            prev = current
            current = current.next
            i += 1

        if prev is not None:
            prev.next = current.next
        else:
            head = current.next
        return head

        