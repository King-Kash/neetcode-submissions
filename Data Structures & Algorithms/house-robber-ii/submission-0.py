class Solution:
    def rob(self, nums: List[int]) -> int:

        # Phase 1 - Create memeory array and set the base cases
        m_length = len(nums) + 1
        m = [0] * m_length

        if m_length >= 4:
            m[0] = 0
            m[1] = nums[0]
            m[2] = max(nums[0], nums[1])
            m[3] = max(nums[0], nums[1], nums[2])
        elif m_length >= 3: 
            m[0] = 0
            m[1] = nums[0]
            m[2] = max(nums[0], nums[1])
        elif m_length >= 2:
            m[0] = 0
            m[1] = nums[0]
        else:
            m[0] = 0


        # Phase 2 - Fill out the memory using the recursive relation
        for i in range(4, m_length):
            m[i] = max(nums[i-1] + m[(i+2)%len(nums)], m[(i+1)%len(nums)])
            print(m[i])
        return m[m_length-1]


