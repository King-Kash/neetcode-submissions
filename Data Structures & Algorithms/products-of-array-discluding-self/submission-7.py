class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        For each element in nums, the product of all the numbers excluding the element itself is the product of the prefix
        of the nums up to that element and the postfix of nums after the element. For each element if we can find the prefix
        and postfix we can compute the correct answer.

        We can either store the prefixes and postfixes in dedicated arrays and combine them later or we can do it all in one pass.
        '''

        output = []

        # Phase 1 - compute the prefix for each element
        prefix = 1 #default value of prefix for the very first elemnt is one since the first element does not really have a prefix
        for element in nums:
            output.append(prefix)
            prefix *= element
        
        #phase 2 - compute the postfix for each element and multiply it with that elements corresponding prefix from phase 1
        postfix = 1 #default
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        
        return (output)