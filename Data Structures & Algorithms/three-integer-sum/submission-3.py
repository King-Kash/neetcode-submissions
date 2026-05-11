class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        seen = set()
        for i in range(len(nums) - 2):
            target = -nums[i]
            subset = nums[i+1:]
            for j in range(len(subset)):
                diff = target - subset[j]
                if diff in subset[j+1:]:
                    soln = tuple(sorted([nums[i], subset[j], diff]))
                    if soln not in seen:
                        seen.add(soln)
                        output.append(soln)
        return output
                        

