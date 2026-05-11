class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # the max times any one number can occur is equal to the length of the nums array (i.e. every element in nums array is the same number)
        max_count = len(nums)
        # the index is the frequencies from 0 to max_counts-1, the values stored are the numbers themselves
        frequencies = [[] for _ in range(max_count)]

        # dictionary for inital counts
        number_counts = defaultdict(int)
        for num in nums:
            number_counts[num] += 1

        # fill the frequency buckets with the numbers that have the matching frequency
        for key, value in number_counts.items():
            frequencies[value - 1].append(key)

        index = max_count - 1
        result = []
        while k > 0:
            if frequencies[index]:
                valid_addition = frequencies[index].pop()
                result.append(valid_addition)
                k -= 1
            else:
                index -= 1
        return result




