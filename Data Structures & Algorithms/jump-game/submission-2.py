class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1
        print(end)
        index = 0
        while True:
            jump = nums[index]

            if (jump == 0) and (index != end):
                return False

            index += jump

            if len(nums) == 1:
                return True

            if (index == end):
                return True
            elif (index > end):
                return False
            

        