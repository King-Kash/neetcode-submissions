class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        BFS might be a good option.
        Treat each 0 as the starting point and run a full BFS on the
        entire grid.
        1. Traverse the matrix till you find a 0.
        2. Run DFS from that 0 and fill in the distance each land cell
           is from the 0.
        3. If you find another 0, repeat steps 1 and 2. If a land cell
           already has a distance, the distance to the new 0 must be
           lower in order to replace the existing value.
        '''
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                curr = grid[r][c]
                if curr == 0:
                  queue = [(r,c)]
                  current_level = 0
                  Discovered = {(r,c)}
                  while queue:
                    level_size = len(queue)

                    for _ in range(level_size):
                        node = queue.pop(0)
                        if current_level <= grid[node[0]][node[1]]:
                            grid[node[0]][node[1]] = current_level

                        for dr, dc in directions:
                            nr = node[0] + dr
                            nc = node[1] + dc
                        
                            if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == -1):
                                continue

                            if (nr, nc) not in Discovered:
                                Discovered.add((nr, nc))
                                queue.append((nr,nc))
                    
                    current_level += 1

        for r in range(len(grid)):
            curr = grid[r]
            print(curr)

                    