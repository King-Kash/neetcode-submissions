class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        min_rate = 1
        res = max_rate
        while min_rate < max_rate:
            rate = (min_rate + max_rate) // 2
            hours = 0
            for pile in piles:
                if pile < rate:
                    hours +=1
                else:
                    hours += -(-pile//rate)
            if hours > h:
                min_rate = rate + 1
            elif hours <= h:
                max_rate = rate - 1
                if rate <= res:
                    res = rate
        return res 