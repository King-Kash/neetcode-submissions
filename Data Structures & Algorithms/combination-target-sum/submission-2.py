class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        To avoid the duplicates we need to restrict the use of any options in nums before the current option
        in the rcursive call. For example if nums is [2,5,6,9] and in our loop option is currently at 5 then in the
        recursive call made for that iteration we must pass in nums = [5, 6, 9]. In this way there is no possibility
        of considering a solution with 5 and 2 in this branch. Rather any solutions with 5 and 2 will be found from
        the branch when option = 2. We must apply this same logic at every level of the recursive tree to avoid duplicates.
        '''
        
        # Phase 1 - handle the base case
        if target == 0:
            return [[]]
        if target < min(nums):
            return None
        

        # Phase 2 - handle the recursion
        result = []
        for i, option in enumerate(nums):
            nxt_target = target - option
            nxt_nums = nums[i:]
            res = self.combinationSum(nxt_nums, nxt_target)
            print(target, res)
            if res is not None:
                for arr in res:
                    if arr is not None:
                        arr.append(option)
                        result.append(arr)
        return result