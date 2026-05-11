# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Run BFS to get to subRoot starting val in the main Root tree. Then run the DFS algorithim
        from the same tree problem to check if the substructures and values match. 
        '''
        
        # Base Cases
        if not root and not subRoot:
            return True
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False
        
        if root.val != subRoot.val:
            return (self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot))
        
        res = self.sameTree(root, subRoot)
        if not res:
            return (self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot))
        return res

        
       
    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.sameTree(p.right, q.right) and self.sameTree(p.left, q.left))
            


