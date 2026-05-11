class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        while i < n:
            max_jump = nums[i]
            if (max_jump == 0) and (i != (n-1)):
                return False

            target = 0
            j = 1
            while (j <= max_jump) and (target == 0):
                if (i+j) >= n-1:
                    return True
                target = nums[i]
                j+=1
            
            if target == 0:
                return False

            i += target
            if (i >= (n-1)):
                return True

            

        