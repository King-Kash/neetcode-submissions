class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Phase 1 - We must sort first because the cars need to be arranged in decreasing order of their positions
        # NOTE: The speeds need to be reordered in the exact fasion as the positions to keep the 1-to-1 correspondance
        combined = zip(position, speed)
        sorted_comb = sorted(combined, key=lambda x: x[0])
        for i, comb in enumerate(sorted_comb):
            position[i] = comb[0]
            speed[i] = comb[1]

        count = 0
        while position:
            for i in range(len(position)):
                position[i] += speed[i]
            if position[-1] >= target:
                count += 1
                last_pos = position.pop()
                last_speed = speed.pop()
                while position and position[-1] >= target:
                    current_pos = position.pop()
                    current_speed = speed.pop()
                    if current_pos < last_pos:
                        count += 1
        return count
                