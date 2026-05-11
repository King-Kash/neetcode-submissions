class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Phase 1 - We must sort first because the cars need to be arranged in decreasing order of their positions
        # NOTE: The speeds need to be reordered in the exact fasion as the positions to keep the 1-to-1 correspondance
        combined = zip(position, speed)
        sorted_comb = sorted(combined, key=lambda x: x[0], reverse=True)
        count_hash = defaultdict(list)
        for i in range(len(position)):
            count = 0
            pos = sorted_comb[i][0]
            while pos < target:
                count += 1
                pos += sorted_comb[i][1]
            count_hash[count].append(i)
        return len(count_hash.keys())
        