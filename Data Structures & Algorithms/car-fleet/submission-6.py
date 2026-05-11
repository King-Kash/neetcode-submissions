class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Phase 1 - We must sort first because the cars need to be arranged in decreasing order of their positions
        # NOTE: The speeds need to be reordered in the exact fasion as the positions to keep the 1-to-1 correspondance
        combined = zip(position, speed)
        sorted_comb = sorted(combined, key=lambda x: x[0], reverse=True)
        for i, comb in enumerate(sorted_comb):
            position[i] = comb[0]
            speed[i] = comb[1]


        times = []
        count = 0
        for i in range(len(position)):
            time = (target - position[i])/speed[i]
            times.append(time)

        res = []
        res.append(times[0])
        prev_time = times[0]
        for time in times:
            if time > prev_time:
                res.append(time)
                prev_time = time
        return len(res)



            


