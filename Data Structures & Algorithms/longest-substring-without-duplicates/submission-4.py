class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        curr_count = 0
        max_count = 0
        current = {}
        length = len(s)
        while ( (start <= end) and (start < length) ):
            if (s[end] in current):
                start = current[s[end]] + 1
                # curr_count = (end - current[s[end]])
                curr_count = 0
                current = {}
                end = start
            else:
                current[s[end]] = end
                curr_count += 1
                if (curr_count >= max_count):
                    max_count = curr_count
                
                #print(current)

                if (end < length - 1):
                    end += 1
                else:
                    start += 1
            

            
        
        return max_count


    # declare max and current count 
    # declare two pointers for the start and end of window
    # declare length of the string
    # while start <= end and start < length of string
    #     check if letter pointed at by end ptr is in the hash
    #         yes: move start pointer to the end pointers position and reset the current count to 0
    #         no: add the char to the hash, increment count, check if current count larger than max
    #     if end pointer is less than length of string minus one
    #         move it forward
    #     else 
    #         move the start pointer forward

        