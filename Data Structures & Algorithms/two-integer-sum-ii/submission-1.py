class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        retArray = []
        i = 0
        for i in range(len(numbers) - 1):
            j = i+1
            for j in range(len(numbers)):
                if(numbers[i] + numbers[j] == target):
                    retArray.append(i+1)
                    retArray.append(j+1)
                    return retArray
        return retArray
        
            


        