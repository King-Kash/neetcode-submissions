class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        Discovered = set()
        queue = []
        ROWS = len(grid)
        COLS = len(grid[0])
        one_found = False

        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    Discovered.add((r,c))
                if grid[r][c] == 1:
                    one_found = True
        
        if len(queue) == 0:
            if one_found:
                return -1
            return 0
                    
        timer = 0
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                current = queue.pop(0)
                r = current[0]
                c = current[1]
                                
                grid[r][c] = 2
                
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == 2 or grid[nr][nc] == 0:
                        continue

                    
                    if (nr, nc) not in Discovered:                        
                        queue.append((nr, nc))
                        Discovered.add((nr,nc))
            
            timer += 1

        res = timer - 1
        for r in range(ROWS):
            print(grid[r])
            for c in range(COLS):
                if grid[r][c] == 1:
                    res = -1
        
        return res
            
