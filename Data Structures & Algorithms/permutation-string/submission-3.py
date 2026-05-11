class Solution:
    '''
        The solution to this problem when approached logically
        dictates the use of a hashmap to count the quantity of
        each char 'a'-'z' in the substring.

        We can use an array though, in place of a hashmap if we
        convert the 26 character into their integer equivalents
        and use those integers as the indecies of the array
    ''' 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        # char counts of s1 that we must match
        s1_arr = [0] * 26
        for char in s1:
            index = ord(char) - ord('a')
            s1_arr[index] += 1
        
        # char counts for the intial subtring from [0, len(s1) - 1]
        substring_arr = [0] * 26
        for i in range(len(s1)):
            index = ord(s2[i]) - ord('a')
            substring_arr[index] += 1
    
        if substring_arr == s1_arr:
            return True
        # matches = 26 # goal is to find a subtring that has equal counts as s1
        # for i in range(len(s1_arr)):
        #     #count matches between the first substring and s1 
        #     if s1_arr[i] != substring_arr[i]:
        #         matches -= 1

        right = len(s1) - 1
        left = 0
        while right < len(s2) - 1:
            # update char counts when window moves
            right += 1
            r_char = ord(s2[right]) - ord('a')
            substring_arr[r_char] += 1

            l_char = ord(s2[left]) - ord('a')
            substring_arr[l_char] -= 1
            left += 1

            #OPTIONS
            # 1. compare the whole arrays -> O(26*n)
            # 2. Update the matches count and check it euqals 26 -> O(n)

            if substring_arr == s1_arr:
                return True
        
        return False


        


    
    

       


        
