class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 0
        max_price = prices[start] - prices[end]
        length = len(prices)
        while(start <= end):
            current_price = prices[end] - prices[start]
            if (current_price >= max_price):
                max_price = current_price
                end += 1
            elif(start <= length):
                start += 1
        return max_price



        