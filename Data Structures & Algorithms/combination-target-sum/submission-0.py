class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Phase 1 - handle the base case
        if target == 0:
            return [[]]
        if target < nums[0]:
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