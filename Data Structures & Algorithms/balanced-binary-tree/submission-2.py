# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        res = self.dfsHelper(root)
        q = []
        q.append(root)
        while q:
            current = q.pop(0)
            if current.balanced == False:
                return False
            if current.right is not None:
                q.append(current.right)
            if current.left is not None:
                q.append(current.left)
        return True
        return max_path
    def dfsHelper(self, root: Optional[TreeNode]):
        max_right_path = 0
        max_left_path = 0
        if root.right is not None:
            max_right_path = self.dfsHelper(root.right)
            max_right_path += 1
        if root.left is not None:
            max_left_path = self.dfsHelper(root.left)
            max_left_path += 1
        diff = (max_left_path - max_right_path)
        print(abs(diff))
        if abs(diff) > 1:
            print('check')
            root.balanced = False
        else:
            root.balanced = True
        print('root:', root.val, 'right:', max_right_path, 'left:', max_left_path, 'balanced:', root.balanced)
        return max(max_left_path, max_right_path)
