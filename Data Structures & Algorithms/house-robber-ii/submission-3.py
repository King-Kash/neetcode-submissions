class Solution:
    def rob(self, nums: List[int]) -> int:
        # # handle the base cases first
        # m = []
        # m.append(0)

        # # fill in the rest of the indecies using the recursive relation
        # for i in range(nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        return max(self.rob(nums[1:n-2]) + nums[n-1], self.rob(nums[:n-1]))



        

