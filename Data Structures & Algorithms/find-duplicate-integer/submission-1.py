class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        largest_seen = 0
        for i in range(len(nums)):
            if nums[i] <= largest_seen:
                return nums[i]
            else:
                largest_seen = nums[i]