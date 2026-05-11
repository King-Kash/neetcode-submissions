class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        next_store = defaultdict(lambda: None)
        for element in nums:
            next_store[element] = element + 1

        max_length = 0
        counter = 0
        for element in nums:
            next_val = next_store[element]
            while next_val is not None:
                counter += 1
                next_val = next_store[next_val]
            if counter >= max_length:
                max_length = counter
            counter = 0
        return max_length
