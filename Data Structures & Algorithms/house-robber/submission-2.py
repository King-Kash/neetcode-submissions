class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        1. Choice Diagram: For the n-th house, you can either rob it or dont rob it. 
            Rob: You could not have robbed the previous house. So the next previous
                 house to consider would be house (n-2). Dont have to worry about blocking
                 off the next house since n is the last house. Moreover since we robbed this
                 house we get the value stored in this house. 
                 Formula: F(n-2) + money[n]

            Don't Rob: We can consider robbing the previous house. We dont get the value for this
                       house since we did not rob it.
                       Formula: F(n-1)
        
        2. Function: F(n) is some imaginary function that tells you the most amount of money you can
                     make by robbing n houses.
        
        3. Recursive Relation:
            From Choice Diagram - F(n) = max(F(n-1), F(n-2) + money[n])
            Base Condition - F(0) = 0, F(1) = money[1]

        4. Turn this recursive setup into an iterative solution using the memory array m.
        '''


        # Phase 1 - Set up the storage array
        length = len(nums) + 1
        m = [0] * (length)
        m[0] = 0
        m[1] = nums[0]

        # Phase 2 - Use the recursive relation to find the max value for i houses
        for i in range(2, len(nums)+1):
            m[i] = max(m[i-1], m[i-2] + nums[i-1])
        
        last = len(m)
        return m[last-1]

