# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #Phase 1 - reverse the linked list
        current = head
        prev = None
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        head = prev

        #Phase 2 - remove the item from the list
        current = head
        prev = None
        for i in range(n-1):
            prev = current
            current = current.next
        
        if prev is not None:
            prev.next = current.next
        else:
            head = current.next

        #Phase 3 - flip the list back to the original ordering
        current = head
        prev = None
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        head = prev
        
        return head
            
