class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        This solution runs in O(n * (n+k)) time which is not good enough for us.
        '''
        # Phase 1 - Count the number frequencies for each element
        frequencies = defaultdict(int)
        for element in nums:
            frequencies[element] += 1

        print(frequencies)
        
        # Phase 2 - Bucket sort using the counts as buckets/index and keys as vals. Bounds size of buckets list
        #           to n because if all n elements were the same then our largest count/bucket/index can 
        #           only be n.
        valid_max = [] 
        for i in range(len(nums)+1):
            valid_max.append([])

        for key in frequencies.keys():
            index = frequencies[key]
            valid_max[index].append(key)

        # Phase 3 - Select the top k keys from the bucket sourt
        top_count = k
        output = []
        for i in range(len(valid_max)-1, -1, -1):
            if (len(valid_max[i]) <= top_count):
                output.extend(valid_max[i])
                top_count -= len(valid_max[i])
            else:
                for j in range(top_count):
                    output.append(valid_macx[i][j])
        
        return output





        
