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

        2. The condition we must check is that using the current rate
        is the total amount of time greater than, less than, or equal
        to the max number of hours we can take.
        a. If hours > h we are working too slow and the rate must be in
        the right half (above current rate).
        b. If hours <= h then this is a valid rate. However we might be
        able to find a smaller rate which would indeed increase the number
        of hours it take to get through the pile but as long as we are below
        h its ok we can keep trying to minimize the rate. Of the valid rates
        we come across we only want the smallest valid one.
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
            elif hours <= h:
                max_rate = rate - 1
                if rate <= res:
                    res = rate
        return res 
