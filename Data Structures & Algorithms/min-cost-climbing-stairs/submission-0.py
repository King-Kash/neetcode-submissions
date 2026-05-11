class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        if n == 0:
            return cost[0]
        if n == 1:
            return cost[1]

        def f(i):
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            
            return cost[i] + min(f(i-1), f(i-2))
        
        return min(f(n-1), f(n-2))
        

        




'''
1. Given a set of steps each with a cost get from the bottom to the top step while paying the
minimum cost.

2. To make the problem smaller we can try to get to an earlier step while paying the least cost 
possible.

3. F(cost) - returns the minimum cost to get to the n-1 step

4. Base Cases - if we are only trying to get to step 0 we must pay the cost for step 0.
            - if we are trying to get to step 1, since we can start at step 1 we just take the
                min cost between step 1 and step 0

5. Recursive Calls: We can make the problem smaller by making target step one less or two less
f(i-1), f(-2)

6. Combine Results = cost[i] + min(f(i-1), f(i-2)) for all steps other than the main full problem
                    we do not pay a cost for the ending because we land just past the final index. 

'''


