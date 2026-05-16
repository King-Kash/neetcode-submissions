class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        def to_num(num):
            digit_num = 0
            for i in range(len(num)):
                curr_num = num.pop()
                digit_num += curr_num * (10 ** (i))
            return digit_num

        def to_arr(num):
            res_arr = []
            while num:
                curr_digit = num % 10
                res_arr.insert(0, curr_digit)
                num = num // 10
            return(res_arr)
        
        digit_num = to_num(digits)
        digit_num += 1
        res_arr = to_arr(digit_num)
        return res_arr