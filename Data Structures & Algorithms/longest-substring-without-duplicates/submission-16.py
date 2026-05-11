class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_chars = defaultdict(int)
        right=0
        left=0
        max_length = 0
        while right < len(s):
            print(s[right])
            current_chars[s[right]] += 1
            while current_chars[s[right]] > 1:
                current_chars[s[left]] -= 1
                left += 1
            right += 1
            length = right - left
            if length > max_length:
                max_length = length

        
        return(max_length)
                 
            

