class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in my_map:
                return [my_map[dif], i]
            else:
                my_map[nums[i]] = i

            
        