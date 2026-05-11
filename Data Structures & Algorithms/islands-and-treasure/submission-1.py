class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        BFS might be a good option.
        1. Traverse the matrix till you find every single 0.
        2. Run BFS from every 0 SIMULTANEOUSLTY and fill in the distance to each 
           cell. This works because every space that is empty is filled by its
           closest gate/zero before any others. When the others do get to a filled
           in cell, the current level will be higher than the one the cell already has. 
        
        - This solution runs in O(m*n) = O(V + E) for a grid. This is the runtim since 
        we run a single BFS despite multiple starting points.
        - This solution uses O(m*n) space due to the Discovered set which stores every grid
        we every discover. (all of them)
        '''
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])


        # Find every gate/zero to begin.
        queue = []
        Discovered = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    Discovered.add((r,c))
        
        # Run BFS from every zero at the same time. Works because every space
        # that is empty is filled by its closest gate/zero before any other
        # zero can reach it.
        current_level = 0
        while queue:
            layer_size = len(queue)

            for _ in range(layer_size):
                curr = queue.pop(0)
                r = curr[0]
                c = curr[1]

                if current_level <= grid[r][c]:
                    grid[r][c] = current_level

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == -1:
                        continue

                    if (nr,nc) not in Discovered:
                        Discovered.add((nr,nc))
                        queue.append((nr,nc))
            current_level += 1



                    