class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        roots = []
        # Phase 1: Find locations of all 0's in the grid
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    roots.append((r,c))

        # Phase 2: Run a DFS simulatenously from each of the roots
            # Add an extra param to pass in the parent nodes count so the child can increase it by one
            # If a node has already been discovered that means it closer to another node no need for fancy logic
        def dfs(roots):
            if not roots:
                return
            
            Explored = defaultdict(bool)
            stack = []
            for root in roots:
                stack.append((root, 0))

            # down, up, right, left
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            
            while stack:
                current = stack.pop()
                current_location = current[0]
                current_val = current[1]
                #  or grid[current_location[0]][current_location[1]] > current_val

                if Explored[current_location] == False or grid[current_location[0]][current_location[1]] > current_val:
                    Explored[current_location] = True
                    grid[current_location[0]][current_location[1]] = current_val
                    for direction in directions:
                        n_r = current_location[0] + direction[0]
                        n_c = current_location[1] + direction[1]
                        if (n_r < len(grid) and n_r >= 0 and n_c < len(grid[0]) and n_c >= 0 and grid[n_r][n_c] != 0 and grid[n_r][n_c] != -1):
                            stack.append(((n_r, n_c), current_val + 1))
                            

        
        dfs(roots)
        print(grid)
        
