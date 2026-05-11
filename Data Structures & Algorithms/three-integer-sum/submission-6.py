class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            target = -1 * nums[i]
            options = nums.copy()
            options.pop(i)

            left = 0
            right = len(options) - 1
            while left < right:
                if options[left] + options[right] == target:
                    result = ([options[left], options[right], nums[i]])
                    result = sorted(result)
                    if result not in res:
                        res.append(result)
                    left += 1
                elif options[left] + options[right] < target:
                    left += 1
                else:
                    right -= 1
        return res