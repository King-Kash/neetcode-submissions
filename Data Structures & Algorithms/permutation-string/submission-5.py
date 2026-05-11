class Solution:
    '''
        The solution to this problem when approached logically
        dictates the use of a hashmap to count the quantity of
        each char 'a'-'z' in the substring.

        We can use an array though, in place of a hashmap if we
        convert the character into their integer equivalents
        and use those integers as the indecies of an array with 26
        positons, one for each letter. The array itself will store
        the counts of the characters.

        Option 1: Is to directly compare all 26 counts of the subtring
                  array to the 26 counts of the s1_arr array.
        Option 2: In order for the substring to be an anagram of the 
                  s1, the counts of all 26 chars needs to be identical.
                  We can intilize how many of the chars actually match 
                  for the first substring. Then we can shift our window
                  updating our matches count each time we move the window.
                  If at anypoint we have exactly 26 matches we have located
                  a permutation of s1
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
    
        # if substring_arr == s1_arr:
        #     return True
            
        matches = 26 # goal is to find a subtring that has equal counts as s1
        for i in range(len(s1_arr)):
            #count matches between the first substring and s1 
            if s1_arr[i] != substring_arr[i]:
                matches -= 1
        
        if matches == 26:
            return True

        right = len(s1) - 1
        left = 0
        while right < len(s2) - 1:
            # update char counts when window moves
            right += 1
            r_char = ord(s2[right]) - ord('a')
            substring_arr[r_char] += 1
            if substring_arr[r_char] == s1_arr[r_char]:
                matches += 1
            else:
                matches -= 1

            l_char = ord(s2[left]) - ord('a')
            prev_l = l_char
            substring_arr[l_char] -= 1
            if substring_arr[l_char] == s1_arr[l_char] and substring_arr[prev_l] == s1_arr[prev_l]:
                matches += 1
            left += 1

            #OPTIONS
            # 1. compare the whole arrays -> O(26*n)
            # 2. Update the matches count and check it euqals 26 -> O(n)

            if matches == 26:
                return True
        
        return False


        


    
    

       


        
