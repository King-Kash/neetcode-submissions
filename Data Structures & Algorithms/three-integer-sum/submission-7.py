class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            target = -1 * nums[i]
            left = i+1 #helps avoid duplicates and the need for sorting because
            # if we could not find a combination with this left that summed to zero when i was an earlier index
            # there is no point considering that previous index again because we already
            # tried and found all the combos that sum to zero. If one or more of them would have
            # included our current left index then it has already been found. By keeping left at i+1 we only ever
            # consider combinations of indecies that have not been seen before.
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    result = ([nums[left], nums[right], nums[i]])
                    if result not in res:
                        res.append(result)
                    left += 1 #careful not to break here since there 
                    # may be multiple combinations that utilize the same
                    # target to achive a sum of 0. ex) target = -3; [-3,0,3], [-3, 1, 2]
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return res