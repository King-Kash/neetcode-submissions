class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
            '''
            NOTE: We dont need to check if an element is already in the top_sort list because
                  the condition to add an elemnt to the zero_queue is that its in_degree must 
                  equal EXACTLY zero. If we have a cycle and revisit a node that was already
                  processed, it in_degree will become negative and it will not be added to the 
                  queue. This will break out of our loop. 
            '''
            neighbors = prerec_for[zero_in]
            for neighbor in neighbors:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    zero_queue.append(neighbor)
        
        if len(top_sort) == numCourses:
            return top_sort
        else:
            return []