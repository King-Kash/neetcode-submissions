class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # if water can flow downhill from a cell to an ocean then the opposite would be the water can flow uphill from the ocean to the cell.
        # from each ocean boarder find all the cells that can be reached if the water flows uphill
        # these cells are equivalentaly all the cells from which water can reach the given ocean
        # repeat for both oceans and the overlapping cells in both sets is the final answer
        def dfs(roots):
            if not roots:
                return []
            
            stack = []
            Explored = defaultdict(bool)

            for root in roots:
                stack.append(root)
            
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            reachable = []
            
            while stack:
                current = stack.pop()
                if not Explored[current]:
                    Explored[current] = True
                    reachable.append(current)
                    
                    for direction in directions:
                        n_r = current[0] + direction[0]
                        n_c = current[1] + direction[1]
                        if n_r < 0 or n_r >= len(heights) or n_c < 0 or n_c >= len(heights[0]):
                            continue
                        if heights[n_r][n_c] >= heights[current[0]][current[1]]:
                            stack.append((n_r,n_c))
            return reachable

        pacific_roots = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or c == 0:
                    root = (r,c)
                    pacific_roots.append(root)
        
        atlantic_roots = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == len(heights)-1 or c == len(heights[0])-1:
                    root = (r,c)
                    atlantic_roots.append(root)
        
        pacific_res = dfs(pacific_roots)
        atlantic_res = dfs(atlantic_roots)

        common = []
        for element in pacific_res:
            if element in atlantic_res:
                common.append([element[0], element[1]])
        
        return common

