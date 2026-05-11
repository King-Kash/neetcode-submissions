class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            currentSum = numbers[i] + numbers[j]
            if currentSum < target:
                i += 1
            elif currentSum > target:
                j -= 1
            elif currentSum == target:
                return [i+1, j+1]