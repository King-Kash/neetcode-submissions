class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Phase 1 - We must sort first because the cars need to be arranged in decreasing order of their positions
        # NOTE: The speeds need to be reordered in the exact fasion as the positions to keep the 1-to-1 correspondance
        combined = zip(position, speed)
        sorted_comb = sorted(combined, key=lambda x: x[0], reverse=True)
        sorted_comb = [list(tup) for tup in sorted_comb]

        # Phase 2 - Stack Logic to count the car fleets
        count = 0
        while sorted_comb:
            for comb in sorted_comb:
                comb[0] += comb[1]
            if sorted_comb[0][0] >= target:
                count += 1
                while sorted_comb[0][0] >= target:
                    sorted_comb.pop(0)
                    if len(sorted_comb) <= 0:
                        break

        return count
        