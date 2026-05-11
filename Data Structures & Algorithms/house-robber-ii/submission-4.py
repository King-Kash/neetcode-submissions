class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Note this is NOT Dynamic Programming. This is purely a recursive solution to validate the recurance relation.
        
        - The recurance call made in the main rob function only works for the very first call, after which we need to revert
          our procedure back to the house robber one problem.
        - We bring back the recursion from house robber one using a helper function.
        '''
        n = len(nums)
        return max(self.rob_help(nums[1:n-2]) + nums[n-1], self.rob_help(nums[:n-1]))

    def rob_help(self, nums: List[int]):

        n = len(nums)

        if n <= 0:
            return 0
        
        return max(self.rob_help(nums[:n-2]) + nums[n-1], self.rob_help(nums[:n-1]))
        


        