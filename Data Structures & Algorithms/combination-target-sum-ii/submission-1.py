class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dp_sum(candidates, target):
            if target == 0:
                return (True, [[]])

            if not candidates or target < min(candidates):
                return (False, [])

            for candidate in candidates:
                if candidate > target:
                    candidates.remove(candidate)
            
            candidates.sort()
    
            ret = []
            for idx, candidate in enumerate(candidates):
                if candidates[idx] == candidates[idx-1] and idx > 0:
                    continue
                new_candidates = candidates[(idx+1):]
                new_target =  target - candidate
                res = dp_sum(new_candidates, new_target)
                if res[0]:
                    for soln in res[1]:
                        soln = [candidate] + soln
                        ret.append(soln)
            if ret:
                return (True, ret)
            else:
                return (False, [])
        
        res = (dp_sum(candidates, target))
        return res[1]