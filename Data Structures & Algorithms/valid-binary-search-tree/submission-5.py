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
        
        #root is simply bound between the max and min (+/-1000 for this problem) using +/- inf for generalization.
        upper_bound = float('inf')
        lower_bound = float('-inf')

        # We will use helper function because we need to pass 3 inputs
        res = self.dfs(root, lower_bound, upper_bound)
        return res

        
    def dfs(self, root, lower_bound, upper_bound):
        if root is None:
            return True

        current = (root.val > lower_bound) and (root.val < upper_bound)

        #everything to the left of current root must be less than root
        left = self.dfs(root.left, lower_bound, root.val)
        #everything to the right of current must be more than root
        right = self.dfs(root.right, root.val, upper_bound)

        return (current and left and right)