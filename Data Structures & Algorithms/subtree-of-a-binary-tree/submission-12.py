# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base conditions
        def dfs_compare(root, subRoot):
            if root == None and subRoot == None:
                return True
            if (root == None and subRoot) or (root and subRoot == None):
                return False
            

            if root.val == subRoot.val:
                res_left = dfs_compare(root.left, subRoot.left)
                res_right = dfs_compare(root.right, subRoot.right)
                if res_left and res_right:
                    return True
            else:
                return False

        def dfs(root):
            if not root:
                return False
            if not subRoot:
                return True
            
            res_curr = dfs_compare(root, subRoot)
            res_left = dfs(root.left)
            res_right = dfs(root.right)
            return (res_curr or res_right or res_left)

        return dfs(root)
        

'''
                    3
            4               5
        1       N       2       N


                    3
                1       2
'''