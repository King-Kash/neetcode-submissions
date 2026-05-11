class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not nums:
            print(nums)
            return [[]]
        
        i = n-1
        res_set = []
        last_element = nums[i]
        res_set.append([last_element])
        
        j=1
        while (i-j >= 0):
            sub_array = []
            sub_array.append(nums[i])
            sub_array.append(nums[i-j])
            sub_array = sorted(sub_array)
            if sub_array not in res_set:
                res_set.append(sub_array)
            j+=1
        
        j=1
        while (i-j >= 0):
            sub_array = nums[(i-j):]
            sub_array = sorted(sub_array)
            if sub_array not in res_set:
                res_set.append(sub_array)
            j += 1
        
        print(res_set)
        return res_set + self.subsets(nums[:-1])

