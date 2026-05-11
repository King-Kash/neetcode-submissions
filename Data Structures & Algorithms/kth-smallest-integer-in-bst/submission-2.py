# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #DFS (In-Order) Iterative Approach
        stack = []
        cur = root
        n = 0

        while cur or stack:
            while cur:
                stack.append(cur) #We will come back after going left first
                cur = cur.left
            
            cur = stack.pop() #Pop once you cant go further left
		    #Process cur as needed
            n += 1
            if n == k:
                return cur.val
            
            #Go ahead to the right and if right node has left children then handle those first.
            cur = cur.right