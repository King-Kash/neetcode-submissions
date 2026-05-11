# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base Cases
        if not root and not subRoot:
            return True
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False
        
        # If both have a val check if they are the same tree
        if self.sameTree(root, subRoot):
            return True
        else:
        #recursively check if the right and left subtrees match subRoot
            return (self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot))

    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.sameTree(p.right, q.right) and self.sameTree(p.left, q.left))
            


