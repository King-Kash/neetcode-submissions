class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        A valid schedule exits if this is a DAG. We can verify if a graph is a DAG by running
        a topological sort. If a valid topological sort exists then we return true, else false.
        To check for a valid top sort, we compare the length of the final top sort to the number
        of input nodes. If the final top sort is too short then we exited early due to a cycle.
        '''
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
        top_sort = []

        for key in in_degree.keys():
            if in_degree[key] == 0:
                zero_queue.append(key)
        
        while zero_queue:
            zero_in = zero_queue.pop(0)
            top_sort.append(zero_in)

            neighbors = prerec_for[zero_in]
            for neighbor in neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_queue.append(neighbor)
        
        return len(top_sort) == numCourses




        



        

