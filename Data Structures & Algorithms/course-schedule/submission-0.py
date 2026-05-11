class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # Build the dictionary containing in-degree counts
        # Build dictionary telling all nodes dependant on a given node. Makes it easier for us to know which nodes to update if one gets deleted
        in_degree = {}
        prerec_for = defaultdict(list)

        for i in range(numCourses):
            in_degree[i] = 0
        
        for course, prerec in prerequisites:
            in_degree[course] += 1
            prerec_for[prerec].append(course)
        
        zero_queue = []
        top_sort = set()

        for key in in_degree.keys():
            if in_degree[key] == 0:
                zero_queue.append(key)
        
        while zero_queue:
            zero_in = zero_queue.pop(0)
            if zero_in in top_sort:
                break
            top_sort.add(zero_in)

            neighbors = prerec_for[zero_in]
            for neighbor in neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_queue.append(neighbor)
        
        return len(top_sort) == numCourses




        



        

