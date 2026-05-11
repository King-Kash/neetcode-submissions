class Solution:
    def isPalindrome(self, s: str) -> bool:
        headPointer = 0
        tailPointer = len(s) - 1
        while(headPointer <= tailPointer):
            if(s[headPointer].isalpha()):
                if(s[tailPointer].isalpha()):
                    if(s[headPointer].lower() != s[tailPointer].lower()):
                        return False
                    else:
                        headPointer += 1
                        tailPointer -= 1
                else:
                    tailPointer -= 1
            else:
                headPointer += 1
        return True


        