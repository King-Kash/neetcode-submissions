class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        if n == 1:
            ret = '()'
            print([ret])
            return [ret]
        
        res = self.generateParenthesis(n-1)
        ret = []
        for string in res:
            for i in range(len(string)):
                new_string = string[:]
                new_string = new_string[:i] + '()' + new_string[i:]
                if new_string in ret:
                    continue
                ret.append(new_string)
        print(ret)
        return ret

            


soln = Solution()
soln.generateParenthesis(3)

'''
1. Define The Problem
- Given an integer n, creat all the possible combinations with that many PAIRS of parenthesis such that each combination is valid

2. How to make the problem strictly smaller
- I can make the problem smaller by making n smaller meaning I will have less combinations to make

3. f(n) will return all the valid combinations we can make with n pairs of parenthesis

4. Base case
- n=1 would only produce one valid string

5. Legal ways to make the problem strictly smaller by one unit of work
 - reduce the size of n by exactly one
 - f(n-1)

6. Combining the results
- Divide the length of the returned string in half then place a () at each index up to the middle.
- We stop at the middle because if we continued to the second half then we would just have an identical mirror of the first half which is useless.
'''
        