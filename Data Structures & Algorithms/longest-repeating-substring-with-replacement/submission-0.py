class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        left = 0
        max_length = 0
        for right in range(len(s)):
            length = (right - left) + 1
            chars[s[right]] += 1
            #check the subarray is valid. length - max(chars) tells us how many other chars need to be replaced to make the whole subarray the most common char
            if (length - max(chars.values())) > k:
                chars[s[left]] -= 1
                left += 1
                length -= 1
            if length > max_length:
                max_length = length
        
        return max_length
