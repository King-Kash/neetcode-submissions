class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        This solution runs in O(n * (n+k)) time which is not good enough for us.
        '''
        frequencies = defaultdict(int)
        for element in nums:
            frequencies[element] += 1
        
        output = []
        for i in range(k):
            largest_key = max(frequencies, key=frequencies.get)
            frequencies[largest_key] = -1
            output.append(largest_key)
        
        return output
            