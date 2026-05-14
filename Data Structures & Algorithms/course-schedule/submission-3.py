class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = {i: 0 for i in range(numCourses)}
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)
            in_degree[v] += 1
        
        # Start with nodes that have zero dependencies
        queue = deque([i for i in in_degree if in_degree[i] == 0])
        order = []
        
        while queue:
            u = queue.popleft()
            order.append(u)
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
                    
        return len(order) == numCourses