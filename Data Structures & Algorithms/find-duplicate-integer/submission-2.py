class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        max_val = max(nums)
        arr = [0] * (max_val+1)
        print(arr)
        for num in nums:
            if arr[num] == 1:
                return num
            else:
                arr[num] = 1
        return -1