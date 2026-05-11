class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        halfway = len(nums)//2
        left = nums[:halfway]
        right = nums[halfway:]
        return min(self.findMin(left), self.findMin(right))


