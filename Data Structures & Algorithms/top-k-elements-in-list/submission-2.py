class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numCount = {}

        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)

        for c in numCount:
            print(f"{c} , {numCount[c]}")

        klargest = []
        for i in range(k):
            greatestKey = -1
            currentMaxCount = None
            for c in numCount:
                if currentMaxCount == None:
                    currentMaxCount = numCount[c]
                    greatesKey = c
                if numCount[c] >= currentMaxCount:
                    currentMaxCount = numCount[c]
                    greatestKey = c
            klargest.append(greatestKey)
            del numCount[greatestKey]
        
        for i in klargest:
            print(i)

        return klargest

                    

