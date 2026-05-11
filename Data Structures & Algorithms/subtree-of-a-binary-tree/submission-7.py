# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        result = True
        def dfs(root, subRoot):
            if root is None and subRoot:
                return False
            if subRoot is None and root:
                return False
            if root is None and subRoot is None:
                return True

            if root.val == subRoot.val:
                print(root.val)
                resLeft = (dfs(root.left, subRoot.left) or dfs(root.left, subRoot))
                resRight = dfs(root.right, subRoot.right) or dfs(root.right, subRoot)
                return (True and resLeft and resRight)
            else:
                resLeft = dfs(root.left, subRoot)
                resRight = dfs(root.right, subRoot)
                return (resLeft or resRight)
        return (dfs(root, subRoot))
            


