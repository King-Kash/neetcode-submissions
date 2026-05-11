# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            q = collections.deque()
            q.append(root)

            lowest_level = 1
            while q:
                node = q.popleft()
                if node:
                    if node.left or node.right:
                        lowest_level += 1
                        q.append(node.left)
                        q.append(node.right)
            return lowest_level
        else:
            return 0
            

        
        
        