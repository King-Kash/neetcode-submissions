class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=1

        if len(s) == 0:
            return 0
            
        max_length = 1
        seen = defaultdict(int)
        length = 1
        while right < len(s):
            char = s[right]
            if seen[char] >= left:
                length = 1
                left = right
            else:
                length += 1
            if length >= max_length:
                max_length = length

            seen[char] = right
            print(seen)
            print(char)
            right += 1
            print(length)
        return max_length

            

