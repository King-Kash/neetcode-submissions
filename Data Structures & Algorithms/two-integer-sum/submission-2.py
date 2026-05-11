class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums:
                idx = nums.index(diff)
                return [i, idx]


''' 
Pick a number, diff = target - num, idx = index(diff), if idx > 0 return i and idx.
'''