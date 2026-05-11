# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        current = head
        carry = 0

        while l1 and l2:
            val1, val2 = 0, 0 
            if l1 is not None:
                val1 = l1.val
            if l2 is not None:
                val2 = l2.val
            
            val_sum = val1 + val2 + carry
            carry = val_sum // 10
            node_val = val_sum % 10

            
            current.val = node_val
            if current.next is not None:
                current = current.next
            l1 = l1.next
            l2 = l2.next

        if l1 is not None:
            while l1:
                val_sum = l1.val + carry
                carry = val_sum // 10
                node_val = val_sum % 10

                current.val = node_val
                if current.next is not None:
                    current = current.next
                l1 = l1.next
            if carry > 0:
                newNode = ListNode()
                newNode.val = carry
                newNode.next = None
                current.next = newNode
        else:
            current.next = l2
            while l1:
                val_sum = l1.val + carry
                carry = val_sum // 10
                node_val = val_sum % 10

                current.val = node_val
                if current.next is not None:
                    current = current.next
                l1 = l1.next
            if carry > 0:
                newNode = ListNode()
                newNode.val = carry
                newNode.next = None
                current.next = newNode
        
        return head


            


