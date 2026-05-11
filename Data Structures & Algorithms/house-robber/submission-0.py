class Solution:
    def rob(self, nums: List[int]) -> int:
        # Phase 1 - Set up the storage array
        length = len(nums) + 1
        m = [0] * (length)
        m[0] = 0
        m[1] = nums[0]

        for i in range(2, len(nums)+1):
            m[i] = max(m[i-1], m[i-2] + nums[i-1])
        
        last = len(m)
        return m[last-1]
