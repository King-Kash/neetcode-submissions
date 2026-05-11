# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q_tree = [[q.val]]
        L=[q]
        while L:
            LN = []
            LN_vals = []
            for current_q in L:
                if current_q is not None:
                    if (current_q.right is not None):
                        LN.append(current_q.right)
                        LN_vals.append(current_q.right.val)
                    else:
                        LN.append(None)
                        LN_vals.append(None)
                    if (current_q.left is not None):
                        LN.append(current_q.left)
                        LN_vals.append(current_q.left.val)
                    else:
                        LN.append(None)
                        LN_vals.append(None)
            q_tree.append(LN_vals)
            L = LN
        print(q_tree)
        p_tree = [[p.val]]
        L=[p]
        while L:
            LN = []
            LN_vals = []
            for current_p in L:
                if current_p is not None:
                    if (current_p.right is not None):
                        LN.append(current_p.right)
                        LN_vals.append(current_p.right.val)
                    else:
                        LN.append(None)
                        LN_vals.append(None)
                    if (current_p.left is not None):
                        LN.append(current_p.left)
                        LN_vals.append(current_p.left.val)
                    else:
                        LN.append(None)
                        LN_vals.append(None)
            p_tree.append(LN_vals)
            L = LN
        print(p_tree)
        if q_tree == p_tree:
            return True
        else:
            return False


            