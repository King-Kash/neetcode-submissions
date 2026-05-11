# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        trackVals = []

        while head:
            if head.val in trackVals:
                return True
            trackVals.append(head.val)
            head = head.next
        
        return False
        