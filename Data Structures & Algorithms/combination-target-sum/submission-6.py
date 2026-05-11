class Solution:
    def __init__(self):
        # Move memo here so it resets for every test case
        self.memo = {}

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Base Cases
        if target == 0:
            return [[]]
        if target < 0 or not nums:
            return None
        
        state = (tuple(nums), target)
        if state in self.memo:
            return self.memo[state]

        result = []

        for i in range(len(nums)):
            # Your logic for reducing nums to avoid duplicates
            if i > 0:
                new_nums = nums[:-i]
            else:
                new_nums = nums
                
            current_num = new_nums[-1]
            new_target = target - current_num
            
            ret = self.combinationSum(new_nums, new_target)
            
            if ret is not None:
                for arr in ret:
                    # Append the new combination to our local result list
                    result.append(arr + [current_num])
        
        # SAVE THE ENTIRE RESULT LIST AFTER THE LOOP
        self.memo[state] = result
        return result