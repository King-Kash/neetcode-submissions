# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if root is None:
                return (True, 0)


            right_res = dfs(root.right)
            left_res = dfs(root.left)

            if right_res[0] and left_res[0]:
                right_count = right_res[1]
                left_count = left_res[1]
                diff = right_count - left_count
                if abs(diff) > 1:
                    print("False1 at root:", root.val)
                    return (False, 0)
                else:
                    return (True, max(right_count, left_count) + 1)
            print("False2 at root:", root.val)
            return (False, 0)

        result = dfs(root)
        return result[0]

        