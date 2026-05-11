class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numCount = {}

        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)

        for c in numCount:
            print(f"{c} , {numCount[c]}")

        klargest = []
        for i in range(k):
            greatestKey = nums[0]
            currentMaxCount = numCount[greatestKey]
            for c in numCount:
                if numCount[c] >= currentMaxCount:
                    currentMaxCount = numCount[c]
                    greatestKey = c
            klargest.append(greatestKey)
            del numCount[greatestKey]
        
        for i in klargest:
            print(i)

        return klargest

                    

