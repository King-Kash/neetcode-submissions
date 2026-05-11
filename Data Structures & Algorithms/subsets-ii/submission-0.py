class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        [1, 1, 2, 2]
        [], [1], [1,1], [2], [1,2], [1, 1, 2]
        def subsets(nums):
            if not nums:
                return ([[]], [[]])
            
            current_num = nums[-1]
            dup = False
            if len(nums) > 1:
                dup = (current_num == nums[-2])
            
            res = subsets(nums[:-1])
            ret = []
            if dup:
                for subset in res[1]:
                    new_arr = subset[:]
                    new_arr.append(current_num)
                    ret.append(new_arr)
            else:
                for subset in res[0]:
                    new_arr = subset[:]
                    new_arr.append(current_num)
                    ret.append(new_arr)
            return (res[0]+ret, ret)
        final = subsets(nums)
        return final[0]
        
        
