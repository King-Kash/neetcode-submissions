# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2
        resList = []

        while (current1 or current2):
            if current1 <= current2:
                resList += current1
                current1 = current1.next
            else:
                resList += current2
                current2 = current2.next

