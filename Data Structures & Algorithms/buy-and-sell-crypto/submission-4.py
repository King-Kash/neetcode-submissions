class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0

        max_profit = 0
        for idx, price in enumerate(prices):
            if price < prices[buy]:
                buy = idx
                sell = idx
            elif price >= prices[sell]:
                sell = idx
            
            max_profit = prices[sell] - prices[buy]

        return max_profit
                