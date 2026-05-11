class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        discovered = []
        island_count = 0
        queue = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1' and (r,c) not in discovered:
                    island_count += 1
                    discovered.append((r,c))
                    queue.append((r,c))
                    while queue:
                        current = queue.pop(0)
                        if current[1]-1 >= 0:
                            if grid[current[0]][current[1]-1] == '1' and (current[0],current[1]-1)  not in discovered:
                                discovered.append((current[0],current[1]-1))
                                queue.append((current[0],current[1]-1))
                        if current[1]+1 < len(grid[0]):
                            if grid[current[0]][current[1]+1] == '1' and (current[0],current[1]+1)  not in discovered:
                                discovered.append((current[0],current[1]+1))
                                queue.append((current[0],current[1]+1))
                        if current[0]-1 >= 0:
                            if grid[current[0]-1][current[1]] == '1' and (current[0]-1,current[1])  not in discovered:
                                discovered.append((current[0]-1,current[1]))
                                queue.append((current[0]-1,current[1]))
                        if current[0]+1 < len(grid):
                            if grid[current[0]+1][current[1]] == '1' and (current[0]+1,current[1])  not in discovered:
                                discovered.append((current[0]+1,current[1]))
                                queue.append((current[0]+1,current[1]))
        return (island_count)










'''
This is the adjaceny matrix representation of a graph.
Same idea with discovered but using a matrix.


'''