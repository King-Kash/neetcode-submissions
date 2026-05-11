class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -1*stone)
        
        print(max_heap)
        
        while len(max_heap) > 1:
            heavy1 = -1*heapq.heappop(max_heap)
            heavy2 = -1*heapq.heappop(max_heap)
            if heavy1 == heavy2:
                continue
            else:
                remaning = abs(heavy1 - heavy2)
                heapq.heappush(max_heap, -1*remaning)
        
        if max_heap:
            return -1*heapq.heappop(max_heap)
        else:
            return 0
