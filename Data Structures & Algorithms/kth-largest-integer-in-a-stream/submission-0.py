class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Place all inital nums into a min-heap
        self.minHeap = nums
        self.k = k # must make k member var to use in add() method

        # Turn the list into a heap
        heapq.heapify(self.minHeap)

        # Remove everything other than the k largest elements
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
         
