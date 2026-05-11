# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = head
        nxt = None
        while(curr != None):
            nxt = curr.next
            print(curr.val)
            if prev != curr:
                curr.next = prev
                prev = curr
            else:
                curr.next = None
            curr = nxt
        head = prev
        return head
        