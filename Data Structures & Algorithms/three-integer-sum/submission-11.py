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
            prev2 = None
            while idx < len(nums):

                val = nums[idx]
                if val == prev2:
                    prev2 = val
                    idx += 1 
                    continue

                diff = 0 - target_val - val
                if diff in visited.keys():
                    pair_idx = visited[diff]
                    final.append([target_val, diff, val])
                else:
                    visited[val] = idx
                idx += 1
                prev2 = val
                
            prev = target_val
            target_idx += 1
        return final
