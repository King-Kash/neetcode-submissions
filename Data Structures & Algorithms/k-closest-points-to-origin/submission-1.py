class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        # Step 1 - Fill the min heap with all the distances
        for point in points:
            distance = ((point[0]**2) + (point[1]**2)) ** 0.5
            heapq.heappush(min_heap, (distance, point))
            
        # Step 2 - Pop off the first K elements, they will be the K smallest.
        solution = []
        for i in range(k):
            element = heapq.heappop(min_heap)[1]
            solution.append(element)
        print(solution)