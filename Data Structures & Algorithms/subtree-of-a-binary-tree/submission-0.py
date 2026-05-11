# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Run DFS on both and see if subroot produces an array that is a subarray of
        the array produced by running BFS/DFS on root.
        '''
        Explored_main = []
        Explored_vals = []
        stack = []
        stack.append(root)
        while stack:
            current = stack.pop()
            if current not in Explored_main:
                Explored_main.append(current)
                Explored_vals.append(current.val)
                if current.right is not None:
                    stack.append(current.right)
                if current.left is not None:
                    stack.append(current.left)
        print(Explored_vals)

        Explored_sub = []
        Explored_sub_vals = []
        stack = []
        stack.append(subRoot)
        while stack:
            current = stack.pop()
            if current not in Explored_sub:
                Explored_sub.append(current)
                Explored_sub_vals.append(current.val)
                if current.right is not None:
                    stack.append(current.right)
                if current.left is not None:
                    stack.append(current.left)
        print(Explored_sub_vals)

        left = 0
        right = len(Explored_sub)
        while right < len(Explored_vals):
            if Explored_vals[left:right] == Explored_sub_vals:
                return True
            right += 1
            left += 1
        return False


