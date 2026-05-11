class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_nums = defaultdict(int)
        print(nums)
        for val in nums:
            dict_nums[val] += 1
        for key, value in dict_nums.items():
            print(value)
        
        res = []
        for i in range(k):
            max_val_key = max(dict_nums, key=dict_nums.get)
            res.append(max_val_key)
            del dict_nums[max_val_key]
        
        return res

        