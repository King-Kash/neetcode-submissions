class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        running_product = 0
        contains_zero = False
        for element in nums:
            if element != 0:
                if running_product == 0:
                    running_product = 1
                    
                running_product *= element
            else:
                contains_zero = True
        
        res_array = []

        for element in nums:
            if element == 0:
                res_array.append(running_product)
            else:
                if contains_zero:
                    res_array.append(0)
                else:
                    res_array.append(int(running_product/element))
        
        return (res_array)