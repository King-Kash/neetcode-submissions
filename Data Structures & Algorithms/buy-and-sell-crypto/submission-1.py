class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dollar value tracker
        min_price = prices[0]
        max_profit = 0

        #pointers
        traveling_pointer = 0
        current_min = 0
       
        length = len(prices)

        if (length <= 1 ):
            return 0;

        while(traveling_pointer < length):
            if(prices[traveling_pointer] < min_price):
                min_price = prices[traveling_pointer]
                current_min = traveling_pointer

            current_profit = prices[traveling_pointer] - min_price

            if (current_profit >= max_profit):
                max_profit = current_profit
            
            traveling_pointer += 1
        print(str(current_min) + ", " + str(traveling_pointer))
        return max_profit



        