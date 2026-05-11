class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token != '+' and token != '-' and token != '*' and token != '/' :
                stack.append(token)
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '/':
                    expression = "".join([num2,token,token,num1])
                else:
                    expression = "".join([num2,token,num1])
                print(expression)
                res = eval(expression)
                print(res)
                stack.append(str(res))
        return int(stack.pop())