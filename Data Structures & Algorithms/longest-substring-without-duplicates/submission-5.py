class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_count = 0
        curr_count = 0
        for char in s:
            if char in char_set:
                if max_count < curr_count:
                    max_count = curr_count
                #reset set
                curr_count = 0
                char_set.clear()
                #restart count
                char_set.add(char)
                curr_count += 1
            else:
                #add to set
                curr_count += 1
                char_set.add(char)
        return (max_count)
            



# use set to store the chars
# start the pointer at the first element and move along
# each time pointer moves we check if that char is in the set
#     if it is then we save the count to max count and reset to 0, clear the set, and store this char in the set
#     if not then incremnet the count and add the element to the set