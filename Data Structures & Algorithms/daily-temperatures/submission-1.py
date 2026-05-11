class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        Stack approach
        '''
        output = []
        stack = []
        for i in range(len(temperatures)):
            output.append(0)
            new_temp = temperatures[i]
            while stack and new_temp > stack[-1][0]:
                stack_item = stack.pop()
                item_index = stack_item[1]
                output[item_index] = (i - item_index)
            stack.append([new_temp, i])
        return output
                
