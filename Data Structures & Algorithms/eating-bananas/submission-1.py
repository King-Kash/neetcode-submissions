class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Switch C - Run Binary Search on the Answer itself
        '''
        1. We must bound the answer itself. The lowest value the
        answer could be is 1. The largest the answer could be is 
        the size of the largest pile. The reason for this is that
        we are limited to eating one pile at a time. If we choose 
        a rate larger than the largest pile we get no benefit. We
        would complete every pile and just have extra rate which is
        not useful when trying to find a minimum rate.

        2. The condition we must check is that 
        '''

        max_rate = max(piles)
        min_rate = 1
        res = max_rate
        while min_rate <= max_rate:
            rate = (min_rate + max_rate) // 2
            hours = 0
            for pile in piles:
                if pile < rate:
                    hours +=1
                else:
                    hours += -(-pile//rate)
            if hours > h:
                min_rate = rate + 1
            elif hours < h:
                max_rate = rate - 1
                if rate <= res:
                    res = rate
            else:
                res = rate
                break

        return res 
