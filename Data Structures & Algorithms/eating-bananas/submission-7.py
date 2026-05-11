class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = -1
        for pile in piles:
            if pile > max_rate:
                max_rate = pile
        
        target_rate = max_rate
        right = max_rate
        left = 1
        while left < right:
            mid = (left + right) // 2
            total_hours = 0
            for pile in piles:
                if pile < mid:
                    total_hours += 1
                else:
                    total_hours += -(-pile // mid)

            if total_hours <= h:
                target_rate = mid
                right = mid
            else:
                left = mid+1
        
        return target_rate