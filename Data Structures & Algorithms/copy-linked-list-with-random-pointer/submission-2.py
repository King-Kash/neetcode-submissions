"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Phase 1 - arrange the original linked list as an array.
        if head == None:
            return None

        array = []
        current = head
        while current is not None:
            array.append(current)
            current = current.next
        
        # Phase 2 - make a copy of each node
        copy_array = []
        current = head
        while current is not None:
            new_node = Node(current.val, None, current.random)
            copy_array.append(new_node)
            current = current.next


        # Phase 3 - link each node to its immediate successor
        for i in range(len(copy_array)-1):
            copy_array[i].next = copy_array[i+1]
        copy_array[-1].next = None

        for i in range(len(copy_array)):
            if copy_array[i].random is not None:
                index = array.index(copy_array[i].random)
                copy_array[i].random = copy_array[index]
            else:
                copy_array[i].random = None

        head_two = copy_array[0]
        return head_two
        # current = head_two
        # while current is not None:
        #     if current.random is not None:
        #         print(f"{current.val}, {current.random.val}")
        #     else:
        #          print(f"{current.val}, {current.random}")
        #     current = current.next

        
        
        
        