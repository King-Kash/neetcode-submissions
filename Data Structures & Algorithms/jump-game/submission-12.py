class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while (i < n):
            max_jump = nums[i]
            if (max_jump == 0) and (i != (n-1)):
                return False
            
            j = i + max_jump
            if j >= n-1:
                return True
            if nums[j] == 0:
                i += 1
                continue
            i = j
        if i >= n-1:
            return True
            
        

            

        