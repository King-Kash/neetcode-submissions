# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is not None) and (q is not None):
            p_q = [p]
            q_q = [q]
            if p.val != q.val:
                return False
            while q_q:
                current_p = p_q.pop(0)
                current_q = q_q.pop(0)
                if (current_p.right is None) ^ (current_q.right is None):
                    return False
                elif (current_p.right is not None) and (current_q.right is not None):
                    if current_p.right.val != current_q.right.val:
                        return False
                    else:
                        p_q.append(current_p.right)
                        q_q.append(current_q.right)

                if (current_p.left is None) ^ (current_q.left is None):
                    return False
                elif (current_p.left is not None) and (current_q.left is not None):
                    if current_p.left.val != current_q.left.val:
                        return False
                    else:
                        p_q.append(current_p.left)
                        q_q.append(current_q.left)
            return True
        elif (p is None) ^ (q is None):
            return False
        else:
            return True

            