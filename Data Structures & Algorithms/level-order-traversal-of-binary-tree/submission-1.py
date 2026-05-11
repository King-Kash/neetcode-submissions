# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        This is literally what binary search does
        '''
        # Base Case:
        if not root:
            return []

        # Main BFS
        queue = [root]
        res = []
        
        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                current = queue.pop(0)
                current_level.append(current.val)

                # Note order matters here because instructions say to go from left to right
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            res.append(current_level)
        
        return res