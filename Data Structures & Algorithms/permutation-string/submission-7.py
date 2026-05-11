class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_arr = [0] * 26
        for char in s1:
            char_idx = ord(char) - ord('a')
            s1_arr[char_idx] += 1

        s1_len = len(s1)
        s2_arr = [0] * 26
        left = 0
        right = 0
        while right < len(s2):
            right_idx = ord(s2[right]) - ord('a')
            s2_arr[right_idx] += 1
            
            if (right - left + 1) > s1_len:
                left_idx = ord(s2[left]) - ord('a')
                s2_arr[left_idx] -= 1
                left += 1
            
            if (s1_arr == s2_arr):
                return True
            
            right += 1
        
        return False
            
