class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for idx, num in enumerate(nums):
            diff = target - num
            if diff in visited.keys():
                pair_idx = visited[diff]
                return [pair_idx, idx]
            else:
                visited[num] = idx
