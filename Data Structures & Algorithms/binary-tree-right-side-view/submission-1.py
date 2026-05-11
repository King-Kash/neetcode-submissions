# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        res = []

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                current = queue.pop(0)
                current_level.append(current.val)

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                
            res.append(current_level[-1])
        return res


