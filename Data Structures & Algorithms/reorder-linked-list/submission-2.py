# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tail = head
        count = 0
        while tail.next is not None:
            count += 1
            tail = tail.next
        print(count)