class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Kashyap Version
        '''
        running_product = 1
        zero_prod = 1
        contains_zero = False
        for element in nums:
            running_product *= element
            if element != 0:
                zero_prod *= element 
            else:
                if contains_zero:
                    zero_prod = 0
                else:
                    contains_zero = True
        
        res_array = []

        for element in nums:
            if element == 0:
                res_array.append(zero_prod)
            else:
                res_array.append(int(running_product/element))
        
        return (res_array)