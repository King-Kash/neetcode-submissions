class Solution:
    memo = []
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        1. Compute all combinations of nums that sum to target 
        2. Make Problem Strictly Smaller:
            We can reduce the number of combinations that sum to target by decreasing the number
            of available nums.
        3. Ideal Function Call:
            cobminationSum(nums, target) returns all the combinations of nums that sum to target
        4. Base Case:
            If the target is 0 we return []
            If the target is below 0 return None
        5. Legal ways to remove one unit of work
            At each step we can remove the last number from the list and see if the remaning numbers
            can sum to the target
        6. Memoization
        '''

        #Base Cases
        if target == 0:
            return [[]]
        if target < 0:
            return None
        if not nums and target > 0:
            return None

        result = []

        for i in range(len(nums)):
            #print(nums[:-i])
            if i > 0:
                new_nums = nums[:-i]
            else:
                new_nums = nums
            current_num = new_nums[-1]
            new_target = target - current_num
            ret = self.combinationSum(new_nums, new_target)
            if ret is not None:
                for arr in ret:
                    arr.append(current_num)
                    result.append(arr)
        return result
        


        
            