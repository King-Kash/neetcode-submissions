# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # #reverse:
        # current = head
        # prev = None
        # while current is not None:
        #     nxt = current.next
        #     current.nxt = prev
        #     prev = current
        #     current = nxt

        # head = prev
        # current = head
        # for i in range(n):

        length = 0
        current = head
        while current is not None:
            current = current.next
            length += 1
        
        index = length - n - 1
        i = 0
        current = head
        prev = None
        while i <= index:
            prev = current
            current = current.next
            i += 1

        if prev is not None:
            prev.next = current.next
        else:
            head = current.next
        return head

        