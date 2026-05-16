class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        one_needed = True
        index = len(digits) - 1
        while index >= 0:
            number = digits[index]
            if one_needed:
                number += 1
            if number > 9:
                number = number % 10
                print(number)
                digits[index] = number
                if index == 0:
                    digits.insert(0, 1)
            else:
                digits[index] = number
                break
            index -= 1
        return digits


            
