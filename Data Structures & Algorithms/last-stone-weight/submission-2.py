class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a min heap but use this little fun trick
        '''
        Usually for a max-heap we multiply everything by -1 to make
        the largest values the smallest. Thus when we pop the largest
        elements from the original list (non-negated) are removed
        leaving smallest original elements in the heap. 

        We can exploit that same trick here. By creating this technically
        "max-heap", we will have the largest values in the top of our heap
        because we put them in negated making them the smallest in the heap.
        When we bring them out we can just flip them back to their original values.
        This means we only ever make the heap once in O(n) time and pop
        from the heap n times. The runtime is down to O(nlogn).
        
        If we did a normal min-heap we would only have two elements in the heap at once and
        after each collision we would have to put all the elements into
        the heap and then pop till we had the two largest. This would
        be O(n^2) operations.
        '''
        
        for idx, stone in enumerate(stones):
            stones[idx] = stone * -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            # Pop the top two
            y = heapq.heappop(stones) * -1
            x = heapq.heappop(stones) * -1
            print(y,x)
            # Run the simulation via if statements
            if y == x:
                continue
            if x < y:
                y = y - x
                y = y * -1
                heapq.heappush(stones, y)
            # If a stone survives put it back into the heap
        
        if len(stones) > 0:
            return (stones[0] * -1)
        return 0