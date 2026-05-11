class Solution:
    def isValid(self, s: str) -> bool:
        opening = 0
        closing = 0
        stack = []
        for c in s:
            if c == '{' or c == '(' or c == '[':
                opening += 1
                stack.append(c)
            else:
                closing += 1
                if closing > opening:
                    return False
                o = stack.pop()
                if c == ")" and o != "(":
                    return False
                elif c == "}" and o != "{":
                    return False
                elif c == "]" and o != "[":
                    return False
        if(opening != closing):
            return False
        return True

            
        

# 3 things to keep track of

# 1. type of bracket must match for closing and opening

# as we iterate through the string have two vars to keep track of the number of opening and closing brackets
# if the number of closing brackets is ever more than the number of opening brackets return false immediately

# 2 and 3. order and type of brackets appearing has to be correct

# iterate through sting
# if a char is open bracket add it to the stack
# if a char is a closed bracket it pop the top of the stack and check that the popped element is the corresponding
# opening element.
