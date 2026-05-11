# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curPointer1 = list1
        curPointer2 = list2

        if curPointer1 and curPointer2:
            if curPointer1.val <= curPointer2.val: 
                head = curPointer1
                curPointer1 = curPointer1.next
            else:
                head = curPointer2
                curPointer2 = curPointer2.next
        elif curPointer1:
            return curPointer1
        else:
            return curPointer2
            
        resPointer = head

        while curPointer1 and curPointer2:
            if curPointer1.val <= curPointer2.val:
                resPointer.next = curPointer1
                curPointer1 = curPointer1.next
                resPointer = resPointer.next
            else:
                resPointer.next = curPointer2
                curPointer2 = curPointer2.next
                resPointer = resPointer.next
        
        if curPointer1:
            resPointer.next = curPointer1
        elif curPointer2:
            resPointer.next = curPointer2

        return head



# assign the head pointer to smaller starting node
# loop through the remaining nodes till only at least on of them hits a null
# add the remaining of the other list to the running list

