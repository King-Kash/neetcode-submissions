class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers) - 1):
            diff = target - numbers[i]
            for j in range(i+1, len(numbers)):
                if numbers[j] == diff:
                    return [i+1,j+1]

        