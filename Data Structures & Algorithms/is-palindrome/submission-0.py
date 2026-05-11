class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s)-1

        while(i<=j):
            if(s[i] != s[j]):
                return false;
            i += 1;
            j -= 1;

        return true;

        