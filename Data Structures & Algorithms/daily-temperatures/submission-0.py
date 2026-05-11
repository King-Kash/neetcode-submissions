class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)-1):
            val = temperatures[i]
            res.append(0)
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > val:
                    res[i] = (j - i)
                    break
        res.append(0)
        return res