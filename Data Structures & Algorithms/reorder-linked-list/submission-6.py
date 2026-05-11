# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #Phase 1 - Split the list in half using the fast and slow pointer method
        slow = head
        fast = head.next

        while (fast) and (fast.next):
            slow = slow.next
            fast = fast.next.next

        l2 = slow.next
        slow.next = None

        #Phase 2 - Reverse the list
        current = l2
        prev = None
        while current is not None:
            temp_next = current.next
            current.next = prev
            prev = current
            current = temp_next
        l2 = prev

        #Phase 3 - Merge the two lists together
        counter = 0
        l1 = head
        current = head
        while (current is not None):
            if counter%2 == 0:
                l1 = l1.next
                current.next = l2
                current = current.next
            else:
                l2 = l2.next
                current.next = l1
                current = current.next
            counter +=1

        # print(counter)



