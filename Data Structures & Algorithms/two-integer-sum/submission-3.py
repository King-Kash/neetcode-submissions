class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in visited:
                idx = visited[diff]
                return [idx, i]
            else:
                visited[nums[i]] = i


''' 
Pick a number, diff = target - num, idx = index(diff), if idx > 0 return i and idx.
'''