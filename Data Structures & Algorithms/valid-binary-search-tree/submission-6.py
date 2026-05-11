# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        right = self.isValidBST(root.right)
        left = self.isValidBST(root.left)

        resLeft = True
        resRight = True
        if root.left:
            left_max = self.dfs_max(root.left)
            resLeft = (left_max < root.val)
        if root.right:
            right_min = self.dfs_min(root.right)
            resRight = (right_min > root.val)
        res = resLeft and resRight
        return (res and right and left)

    def dfs_min(self, root):
        if root is None:
            return 1001

        right, left = 1001, 1001
        if root.right:
            right = self.dfs_min(root.right)
        if root.left:
            left = self.dfs_min(root.left)
        
        return min(root.val, right, left)

    def dfs_max(self, root):
        if root is None:
            return -1001

        right, left = -1001, -1001
        if root.right:
            right = self.dfs_max(root.right)
        if root.left:
            left = self.dfs_max(root.left)
        
        return max(root.val, right, left)









