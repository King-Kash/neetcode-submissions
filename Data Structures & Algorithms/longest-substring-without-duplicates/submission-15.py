class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        length = 0
        seen = {}
        max_length = 1

        if len(s) <= 1:
            return len(s)
            
        while right < len(s):
            char = s[right]
            if (char in seen) and (seen[char] >= left):
                left = seen[char] + 1
                length = (right - left) + 1
            else:
                length += 1
            seen[char] = right
            if length >= max_length:
                max_length = length
            right += 1
        return max_length

            

