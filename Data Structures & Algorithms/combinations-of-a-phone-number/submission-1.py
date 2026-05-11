class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digidict = {
            1: [''],
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t','u', 'v'],
            9: ['w', 'x', 'y', 'z'],
            0: [''],
        }


        def recurse(digits, digidict):
            if not digits:
                return ['']
            
            current_digit = digits[-1]
            remaining_digits = digits[:-1]
            res = recurse(remaining_digits, digidict)
            char_list = digidict[int(current_digit)]
            ret = []
            for char in char_list:
                for string in res:
                    new_string = string + char
                    ret.append(new_string)
            return ret
        
        res = recurse(digits, digidict)
        if res[0] != "":
            return res
        return [] 
            

