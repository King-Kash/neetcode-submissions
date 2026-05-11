class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        result = []
        for i in range(len(nums)):
            # if the outter loop number is positive then then everything that follows will be positive and the sum can not be 0.
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    right = len(nums) - 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif sum < 0:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return (result)

