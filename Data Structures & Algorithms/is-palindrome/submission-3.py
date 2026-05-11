class Solution:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s)-1

        while(i<=j and j>=i):
            if(s[i].isalpha()):
                if(s[j].isalpha()):
                    if(s[i].lower() != s[j].lower()):
                        return False;
                    else:
                        i += 1
                        j -= 1
                else:
                    j -= 1;     
            else:
                i += 1
        return True;

        