class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=1

        max_length = 0
        seen = defaultdict(int)
        length = 1
        while right < len(s):
            if length >= max_length:
                max_length = length
            char = s[right]
            if seen[char] >= left:
                length = 1
                left = right
            else:
                length += 1

            seen[char] = right
            print(seen)
            print(char)
            right += 1
            print(length)
        return max_length

            

