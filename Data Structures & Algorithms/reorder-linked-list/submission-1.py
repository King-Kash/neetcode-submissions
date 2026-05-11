# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        head_list = slow
        fast = head
        while fast and fast.next:
            slow = slow.next         # move slow pointer one step
            fast = fast.next.next    # move fast pointer two steps
        

        tail_list = slow.next
        slow.next = None
        current = tail_list
        prev = None
        while (current):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        tail_list = prev

        dummy = ListNode()
        tail = dummy
        iteration = 0

        while tail_list and head_list:
            if iteration % 2 == 0:
                tail.next = head_list
                tail = tail.next
                head_list = head_list.next
                iteration += 1
            else:
                tail.next = tail_list
                tail = tail.next
                tail_list = tail_list.next
                iteration += 1
        
        if tail_list:
            tail.next = tail_list
        elif head_list:
            tail.next = head_list


        









        
        