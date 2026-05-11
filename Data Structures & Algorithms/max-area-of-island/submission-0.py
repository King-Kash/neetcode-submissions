class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        discovered = []
        max_area = 0
        queue = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in discovered:
                    print((r,c))
                    current_area = 0
                    discovered.append((r,c))
                    queue.append((r,c))
                    while queue:
                        current = queue.pop(0)
                        current_area += 1
                        if current[1]-1 >= 0:
                            if grid[current[0]][current[1]-1] == 1 and (current[0],current[1]-1)  not in discovered:
                                discovered.append((current[0],current[1]-1))
                                queue.append((current[0],current[1]-1))
                        if current[1]+1 < len(grid[0]):
                            if grid[current[0]][current[1]+1] == 1 and (current[0],current[1]+1)  not in discovered:
                                discovered.append((current[0],current[1]+1))
                                queue.append((current[0],current[1]+1))
                        if current[0]-1 >= 0:
                            if grid[current[0]-1][current[1]] == 1 and (current[0]-1,current[1])  not in discovered:
                                discovered.append((current[0]-1,current[1]))
                                queue.append((current[0]-1,current[1]))
                        if current[0]+1 < len(grid):
                            if grid[current[0]+1][current[1]] == 1 and (current[0]+1,current[1])  not in discovered:
                                discovered.append((current[0]+1,current[1]))
                                queue.append((current[0]+1,current[1]))
                    if current_area >= max_area:
                        max_area = current_area
        return max_area
