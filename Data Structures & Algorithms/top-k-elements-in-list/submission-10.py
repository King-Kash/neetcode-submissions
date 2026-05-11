class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Perform Bucket Sorting using the frequencies as the bins.

        1. Count the frequencies of each element and store them in a hashmap.
        2. The freqencies will be used as the index for a list storing a list of all the elements with that freqency
        3. We go from the end of the list and take the top element working our way backwards till k elements have been taken
        '''

        frequencies = defaultdict(int)
        max_frequency = -1
        for num in nums:
            frequencies[num] += 1
            if frequencies[num] > max_frequency:
                max_frequency = frequencies[num]
        
        bins = []
        for _ in range(len(nums)+1):
            bins.append([])

        for key in frequencies.keys():
            index = frequencies[key]
            bins[index].append(key)

        res = []
        top_frequency = len(bins) - 1
        while k > 0:
            vals = bins[top_frequency]
            while vals and k > 0:
                res.append(vals.pop())
                k -= 1
            top_frequency -= 1
        
        return res
