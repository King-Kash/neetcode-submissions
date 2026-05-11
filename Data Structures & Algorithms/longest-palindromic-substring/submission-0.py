class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        def is_pal(i: int, j: int) -> bool:
            # returns True if s[i..j] (inclusive) is palindrome
            if i >= j:                  # length 0 or 1
                return True
            if s[i] != s[j]:
                return False
            # s[i] == s[j], check inner substring
            return is_pal(i + 1, j - 1)

        best_i, best_j = 0, 0
        best_len = 1

        # Check all intervals (i,j) with i<=j
        for i in range(n):
            for j in range(i, n):
                if is_pal(i, j):
                    cur_len = j - i + 1
                    if cur_len > best_len:
                        best_len = cur_len
                        best_i, best_j = i, j

        return s[best_i: best_j + 1]
