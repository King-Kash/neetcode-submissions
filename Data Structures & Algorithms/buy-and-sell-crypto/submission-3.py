class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_ptr = 0
        sell_ptr = 0
        profit = prices[sell_ptr] - prices[buy_ptr]
        while sell_ptr < len(prices):
            if profit <= 0:
                profit = 0

            if prices[sell_ptr] < prices[buy_ptr]:
                buy_ptr = sell_ptr
            
            curr_profit = prices[sell_ptr] - prices[buy_ptr]
            if curr_profit > profit:
                profit = curr_profit
            print(profit, sell_ptr)
            sell_ptr += 1
            
        return profit



            

            

        