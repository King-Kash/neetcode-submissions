# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfsHelper(root)
        q = []
        q.append(root)
        max_path = 0
        while q:
            current = q.pop(0)
            if current.longest >= max_path:
                max_path = current.longest
            if current.right is not None:
                q.append(current.right)
            if current.left is not None:
                q.append(current.left)
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
        
        node_longest = max_right_path + max_left_path
        root.longest = node_longest
        return max(max_right_path, max_left_path)
        
        



        



'''
Start at an arbitrary node s and walk along the unique path to the farthest node v.

The path from s to v must touch the diameter path A—…—B somewhere (call that first touch point x).
(If it didn’t, you could combine paths and make a cycle—impossible in a tree.)

From x, the diameter goes out in two directions: toward A and toward B. At least one direction is as long as or longer than the segment from x to v.
If either side were strictly longer, then the distance from s to that endpoint would beat the distance from s to v, contradicting that v was farthest from s.

Therefore v can’t sit in the middle of the diameter—it must coincide with an endpoint of some longest path. So v is a diameter endpoint.
'''