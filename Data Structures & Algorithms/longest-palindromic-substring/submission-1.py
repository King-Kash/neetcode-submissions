class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        
        #define a DP, momoized internal function
        memo = {}
        def is_pal(i, j):
            if (i >= j):
                # empty substring - base case
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            
            if s[i] == s[j]:
                memo[(i,j)] = is_pal(i+1, j-1)
                return memo[(i,j)]
            else:
                memo[(i, j)] = False
                return memo[(i, j)]
        
        max_length = -1
        best_indecies = (0, 0)
        for i in range(n):
            for j in range(i, n):
                if is_pal(i, j):
                    length = j - i + 1
                    if length >= max_length:
                        max_length = length
                        best_indecies = (i, j)
        
        return s[best_indecies[0]: best_indecies[1] + 1]

            
        