class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        # Step 1 - Fill the min heap with all the negative distances so the largest end up as the smallest
        for point in points:
            distance = (((point[0]**2) + (point[1]**2)) ** 0.5) * -1
            # We use distance as the value that is compared and store the point along with it in a tuple.
            heapq.heappush(min_heap, (distance, point))
        # Step 2 - If we ever have more than k then remove elements, since we negate distance the smallest will be negative of the largest distance
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        # Extract the coordinate point from each element in min_heap
        soln = []
        for element in min_heap:
            soln.append(element[1])
        return soln