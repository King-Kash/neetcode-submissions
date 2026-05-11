# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        head = None
        current = None

        if list1.val <= list2.val:
            head = list1
        else:
            head = list2
        
        current = head

        while (list1 is not None) and (list2 is not None):
            if list1.val <= list2.val:
                list1 = list1.next
                current.next = list2
                current = current.next
            else:
                list2 = list2.next
                current.next = list1
                current = current.next
        
        if list1:
            current.next = list1.next
        elif list2:
            current.next = list2.next
        
        return head