class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     '''
    #     Note this is NOT Dynamic Programming. This is purely a recursive solution to validate the recurance relation.
        
    #     - The recurance call made in the main rob function only works for the very first call, after which we need to revert
    #       our procedure back to the house robber one problem.
    #     - We bring back the recursion from house robber one using a helper function.

    #      NOTE: While this non-memoized solution technically is correct the recursive stack gets so deep and it is so inefficent that you wont pass.
    #     '''
    #     # Base Cases
    #     n = len(nums)
    #     return max(self.rob_help(nums[1:n-2]) + nums[n-1], self.rob_help(nums[:n-1]))

    # def rob_help(self, nums: List[int]):

    #     n = len(nums)

    #     if n <= 0:
    #         return 0
        
    #     return max(self.rob_help(nums[:n-2]) + nums[n-1], self.rob_help(nums[:n-1]))
        

    def rob(self, nums: List[int]) -> int:
        '''
        Note this is Dynamic Programming. When going bottom up you can apply the same idea but rather than 
        deciding if you will keep the last item or not as in the recursive approach, you will choose whether
        to keep the first item or not.
        '''
        if not nums:
            return 0

        n = len(nums)

        if n == 1:
            return nums[0]
        
        case1 = nums[:-1] # We chose first element so must exclude the last element
        case2 = nums[1:] # We did not choose the first element so last element remains a valid option
        return max(self.rob_help(case1), self.rob_help(case2))

    def rob_help(self, nums):
        # Base Case
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        m = [0] * (n + 1)
        m[0] = 0
        m[1] = nums[0]
        m[2] = max(nums[0], nums[1])


        for i in range(3, n+1):
            m[i] = max(m[i-2] + nums[i-1], m[i-1])

        return m[-1]

