class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = {}
        for i in range(numCourses):
            in_degree[i] = 0
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
            in_degree[v] += 1
        
        # Start with nodes that have zero dependencies
        zero_list = []
        for i in in_degree:
            if in_degree[i] == 0:
                zero_list.append(i)
        queue = deque(zero_list)
        order = []
        
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        return len(order) == numCourses