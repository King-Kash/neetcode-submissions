class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for point in points:
        # compute the distance of each point to (0,0)
            distance = ((point[0] - 0)**2 + (point[1] - 0)**2)**0.5
        # store (distance, array) in the hashSet
            heapq.heappush(min_heap, (distance*-1, point))
        # NOTE!!: Since distance is first in the tuple, it will be used when storing order

        while len(min_heap) > k:
            heapq.heappop(min_heap)

        res = []
        while len(min_heap) > 0:
            point = heapq.heappop(min_heap)
            res.append(point[1])
        
        return res
        
