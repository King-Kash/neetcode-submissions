class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        Explored = defaultdict(bool)
        island_count = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(root):
            stack = []
            stack.append(root)

            while stack:
                current = stack.pop()
                if Explored[current] == False:
                    Explored[current] = True
                    curr_row = current[0]
                    curr_col = current[1]
                    for direction in directions:
                        new_row = curr_row + direction[0]
                        new_col = curr_col + direction[1]
                        if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]) or grid[new_row][new_col] == "0":
                            continue
                        neighbor = (new_row, new_col)
                        stack.append(neighbor)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == "1" and Explored[(row, col)] == False:
                    island_count += 1
                    root = (row, col)
                    dfs(root)
        
        return island_count
        
               