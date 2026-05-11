class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_ptr = 0
        right_ptr = 0
        substring = []
        curr_length = 0
        max_length = 0
        for idx, char in enumerate(s):
            if char in substring:
                index = substring.index(char)
                left_ptr += index+1
                substring=substring[index+1:]
                substring.append(char)
                curr_length = len(substring)
            else:
                substring.append(char)
                curr_length=len(substring)
                if curr_length > max_length:
                    max_length = curr_length

        print(substring)
        return (max_length)


            



'''
substring to store the current substring
max_count
curr_count
left_ptr
right_ptr
move the right pointer by one
check if the char is in the subtring
if yes then 
    find index of that char in the subtring
    move the left pointer to index + 1, the substring should be truncated to sub[index+1:], add the current element to the end of the subtring the current length should be updated.
else:
    append the char to the subtring
    update curr_length
    update max_length if curr_length is larger

'''