# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        current_mOne = None

        if (current == None):
            return head

        while current is not None:
            next_node = current.next
            current.next = current_mOne
            current_mOne = current
            current = next_node

        head = current_mOne
        return head
            



# declare current pointer
# declare current-1 pointer

# move the current pointer forward
# set current.next to current-1 
# set current-1 = current
# set current = current.next

# keep repeating this process until current = null
# set head = current-1

        