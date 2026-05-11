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
            resLeft = (root.left.val < root.val)
        if root.right:
            resRight = (root.right.val > root.val)
        res = resLeft and resRight

        return (right and left and res)