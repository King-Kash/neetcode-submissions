class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We can solve this problem with a basic min_heap.

        min_heap = []

        for val in nums:
            heapq.heappush(min_heap, val)
        
        while len(min_heap) > k:
            heapq.heappop(min_heap) 

        return min_heap[0]