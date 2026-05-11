"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Will implement solution with a bredth first search.
        Be aware of how to implement a deep copy correctly using dict.
        '''
        if node is None:
            return None

        queue = [node]
        Discovered = {node} # Using a disctionary cuts the search time to O(1)
        copies = {node: Node(node.val)} # deep copy = dict of {original: new_copy}
        while queue:
            curr = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor not in Discovered:
                    copies[neighbor] = Node(neighbor.val) # create the new node when we discover the node for the first time
                    Discovered.add(neighbor)
                    queue.append(neighbor)
                copies[curr].neighbors.append(copies[neighbor]) # need to make sure the neighbor is counted both times A <-> B in A's list and B's list.
        
        return copies[node]
                    
