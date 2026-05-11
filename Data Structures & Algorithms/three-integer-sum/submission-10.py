class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target_idx = 0
        final = []
        prev = None
        while target_idx < len(nums)-1:
            target_val = nums[target_idx]

            if target_val == prev:
                prev = target_val
                target_idx += 1
                continue

            visited = {}
            idx = target_idx+1
            while idx < len(nums):
                diff = 0 - target_val - nums[idx]
                if diff in visited.keys():
                    pair_idx = visited[diff]
                    final.append([target_val, nums[pair_idx], nums[idx]])
                else:
                    visited[nums[idx]] = idx
                idx += 1
            prev = target_val
            target_idx += 1
        return final
