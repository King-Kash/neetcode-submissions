class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We can solve this problem with a max_heap approach
        '''
        Again, in a max heap the numbers at the top will be the
        invereted versions of the largest numbers. In this way we
        can use a max heap if we need to spit out the largest numbers
        one by one for processing. We just negate them back to their 
        original vals and now we have a sorted order of the largest values

        '''
        
        # max_heap = []

        # for num in nums:
        #     heapq.heappush(max_heap, num*-1)
        
        # last_out = float("-inf")
        # while k > 0:
        #     num = heapq.heappop(max_heap)*-1
        #     print(num)
        #     if num != last_out:
        #         last_out = num 
        #         k -= 1
            
        # return int(last_out)

        # 1. Initialize
        min_heap = []

        # 2. Process Data
        for val in nums:
            # Always push
            heapq.heappush(min_heap, val)
            
            # Maintain the 'Window' of size K
            if len(min_heap) > k:
                heapq.heappop(min_heap) # Smallest is gone

        # 3. Final State
        # min_heap now contains the K LARGEST elements
        return min_heap[0]