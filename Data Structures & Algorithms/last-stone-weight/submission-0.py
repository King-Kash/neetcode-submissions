class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a max heap
        for idx, stone in enumerate(stones):
            stones[idx] = stone * -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            # Pop the top two
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1

            # Run the simulation via if statements
            if y == x:
                continue
            if x < y:
                y = y - x
                heapq.heappush(stones, y)
            # If a stone survives put it back into the heap
        
        if len(stones) > 0:
            return stones[0]
        return 0