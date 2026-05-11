# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_prev):
            if root is None:
                return 0

            if root.val >= max_prev:
                return 1 + dfs(root.right, root.val) + dfs(root.left, root.val)
            else:
                return dfs(root.right, max_prev) + dfs(root.left, max_prev)
        
        return dfs(root, root.val)