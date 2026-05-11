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
        
        current1 = list1
        current2 = list2
        head = None
        while (list1.next is not None) and (list2.next is not None):
            if list1.val <= list2.val:
                list1 = list1.next
                current1.next = list2
                if head is None:
                    head = current1
                current1 = list1
            else:
                list2 = list2.next
                current2.next = list1
                if head is None:
                    head = current2
                current2 = list2

        if (list1.next is None) and (list2.next is not None):
            list2 = list2.next
            current2.next = list1
            current2 = list2
            list1.next = list2
        elif (list2.next is None) and (list1.next is not None):
            list1 = list1.next
            current1.next = list2
            current1 = list1
            list2.next = list1
        return head
