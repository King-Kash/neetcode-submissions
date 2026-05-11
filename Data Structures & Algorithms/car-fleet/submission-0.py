class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count_hash = defaultdict(list)
        for i in range(len(position)):
            count = 0
            pos = position[i]
            while pos < target:
                count += 1
                pos += speed[i]
            count_hash[count].append(i)
        return len(count_hash.keys())
