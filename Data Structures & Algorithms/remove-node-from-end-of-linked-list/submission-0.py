# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        len_finder = head
        num_elements = 0
        while len_finder:
            len_finder = len_finder.next
            num_elements += 1
        
        if n == (num_elements):
            return head.next
        
        current = head.next
        prev = head
        prev_head = prev

        for _ in range(n-1):
            current = current.next
            prev = prev.next
        
        prev.next = current.next
        return prev_head


# loop through the linked list once to find the number of elements in the linked list
# store that in num_elements
# if n == (num_elements)
#     index_to_remove = num_elements mod n handles the loop around

# declare a current and previous pointer
# for _ in range (index_to_remove - 1) since we start pointing to the first element
#     keep moving current next
#     keep moving previous next
# prev.next = current.next





        