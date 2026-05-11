class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_sum = 0
        window_len = len(s1)
        left = 0

        for i in range(window_len):
            target_sum += (ord(s1[i]))
        print(target_sum)

        # Invariant: The window size must be max length of s1
        current_sum = 0
        for right in range(len(s2)):
            current_sum += ord(s2[right])

            while (right - left + 1) > window_len:
                current_sum -= ord(s2[left])
                left += 1
            
            if (right - left + 1) == window_len and current_sum == target_sum:
                return True
        
        return False
            


        
