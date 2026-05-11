# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root is None:
                return False

            result = False
            if root.val == subRoot.val:
                result = dfs_compare(root, subRoot)

            resRight = dfs(root.right)
            resLeft = dfs(root.left)
            return result or resLeft or resRight
            


        def dfs_compare(root, subRoot):
            if root is None and subRoot:
                return False
            if subRoot is None and root:
                return False
            if root is None and subRoot is None:
                return True

            if root.val == subRoot.val:
                resLeft = dfs_compare(root.left, subRoot.left)
                resRight = dfs_compare(root.right, subRoot.right)
                return (True and resLeft and resRight)
            else:
                return False

        return (dfs(root))
           


