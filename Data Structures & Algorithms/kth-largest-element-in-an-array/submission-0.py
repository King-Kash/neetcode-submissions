class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Basic min_heap problem if we sort first

        nums.sort()
        min_heap = []
        for num in nums:
            if len(min_heap) > 0 and min_heap[0] == num:
                continue

            heapq.heappush(min_heap, num)

        while len(min_heap) > k:
            heapq.heappop(min_heap)
        return min_heap[0]