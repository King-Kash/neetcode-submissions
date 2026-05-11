import copy 

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        current_num = nums[-1]
        remaining_nums = nums[:-1]
        subsets = self.subsets(remaining_nums)
        new_subsets = []
        for subset in subsets:
            new_subset = subset + [current_num]
            new_subsets.append(new_subset)
        return subsets + new_subsets

