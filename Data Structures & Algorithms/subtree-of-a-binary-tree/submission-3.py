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
        
        #Outer BFS
        if not root:
            return False
        
        queue = [root]

        res = False
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                current = queue.pop(0)
                if current.val == subRoot.val:
                    # Run DFS to compare structure and values once we find subRoot in the main tree.
                    res = self.sameTree(current, subRoot)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return res
    
    def sameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.sameTree(p.right, q.right) and self.sameTree(p.left, q.left))
            


