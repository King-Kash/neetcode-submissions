class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0

        max_length = 0
        seen = defaultdict(int)
        length = 1
        while right < len(s):
            char = s[right]
            if seen[char] >= left:
                if length >= max_length:
                    max_length = length
                length = 1
                left = right
            else:
                length += 1
            seen[char] = right
            right += 1
        return max_length

            

