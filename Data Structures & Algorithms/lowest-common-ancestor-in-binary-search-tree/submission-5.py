# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Base Cases
        '''
            * From the instructions we are told that we are gaurentted to have p and q in the BINARY
            SEARCH TREE. Due to this fact and the fact that we have a BST there is a finite set of 
            possible situations. 
            * We cant return None since the return must be a TreeNode
            * There is no base case strictly speaking but we can return root when it is null though it wont 
              ever be hit.
        '''
        if not root:
            return root

        # Recursive Steps
        # THESE CASES ARE TRUE BECUASE THIS IS A BST!

        # both p and q are to the left of this node. This node can not be the bridge between p and q
        if (p.val < root.val) and (q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)

        # both p and q are to the right of this node. This node can not be the bridge between p and q
        if (p.val > root.val) and (q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)

        # if root equals either p or q, well then the other MUST be below root. However the only point
        # that bridges the two is root itself.
        if (root.val == p.val) or (root.val == q.val):
            return root
            
        # if one target is to the left of root and the other is to the right of root, then root must be the
        # bridge between the two. There is no way to get from p to q without passing through root.
        if (root.val < p.val and root.val > q.val) or (root.val < q.val and root.val > p.val):
            return root
            