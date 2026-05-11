# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head

        visitedVals = []

        while (current is not None) and (current.val not in visitedVals):
            visitedVals.append(current.val)
            current = current.next
        if current is None:
            return False
        return True
        