class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        NOTE: Written here is the bottom up solution derived from the recursive solution.
        Always solve dp problems using recursive solution then convert that solution to a iterative solution at the end
        Recursive solution:
        1. Draw choice diagram
        2. Pretend you had some imaginary function that solved your problem for you. Decide what you need to pass as inputs into that function.
            In this problem, take f to be the function that tells all the ways to get to the nth step. Well that function needs the input n to do that.
            Our imaginary function that solves the problem for us is f(n).
        3. Turn the choice diagram into a recursive relation that defines f(n) in terms of f(smaller inputs). In other words define our current subproblem
            in terms of smaller subproblems
        4. Find out the base cases for the recursive relationship
        5. Convert the recursive solution to an interative solution.
        '''
        # Phase 1 - Create the array where solution to each subproblem will be stored.
        m = [0] * (n+1)

        # Phase 2 - Fill in the solutions for the subproblems of the base cases
        m[0] = 0
        m[1] = 1
        m[2] = 2

        if n < 3:
            return m[n]
            
        # Phase 3 - Run the loop to fill in the solutions for the remainder of the subproblems using the recursive relation!
        i = 3
        while i < (n+1):
            m[i] = m[i-1] + m[i-2]
            i += 1
        
        return m[n]



        