# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l1=head

        #reverse the list and store that as a seperate linked list called l2
        current=head
        prev=None
        while current is not None:
            temp_next = current.next
            current.next = prev
            prev = current
            current = temp_next
        l2 = prev

        #merge l1 and l2 (original and fliped lists) stopping when the elements from each list have same addr.
        head = l1
        current = head
        counter = 0
        next_up = l2

        while (current != next_up):
            current.next = next_up
            current = current.next
            counter += 1
        
        current.next = None

        while head is not None:
            print(head.val)
            head = head.next

