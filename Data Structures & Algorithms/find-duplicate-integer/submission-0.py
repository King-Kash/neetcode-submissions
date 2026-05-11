class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            val = nums[i]
            count = hashmap[val]
            if count > 0:
                return val
            else:
                count += 1
                hashmap[val] = count
        return 0