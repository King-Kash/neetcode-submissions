class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        This solution runs in O(n * (n+k)) time which is not good enough for us.
        '''
        # Phase 1 - Count the number frequencies for each element
        frequencies = defaultdict(int)
        for element in nums:
            frequencies[element] += 1
        
        # Phase 2 - Go through the elments and only add them to this new array if the
        #           frequency is larger than the current max. If not dont bother cuz that
        #           number has no chance of being the one of the k largest elements. 
        #           When we need to return our output we only need to look at the last k elements
        #           in this list.
        valid_max = []
        max_frequency = 0
        for key in frequencies.keys():
            if frequencies[key] >= max_frequency:
                valid_max.append(key)
                max_frequency = frequencies[key]
        output = valid_max[len(valid_max) - k:]
        print(output)
        
