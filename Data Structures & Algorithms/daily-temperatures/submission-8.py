class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final = [0] * len(temperatures)
        temps_stack = []
        count = 0
        for idx, temp in enumerate(temperatures):
            count += 1
            if not temps_stack:
                temps_stack.append((idx, count))
            else:
                while temps_stack and temp > temperatures[temps_stack[-1][0]]:
                    element = temps_stack.pop()
                    duration = count - element[1]
                    index = element[0]
                    final[index] = duration
                temps_stack.append((idx, count))
        return final



                



