class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers) - 1):
            dif = target - numbers[i]
            j = i+1
            while(j < len(numbers)):
                if numbers[j] == dif:
                    return [i+1, j+1]
                else:
                    j += 1
            i += 1
        