class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        while i < n:
            jump = nums[i]

            if (jump == 0) and (i != (n-1)):
                return False
            if (i == (n-1)):
                return True

            i += jump
