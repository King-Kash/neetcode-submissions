class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            hold_original = nums[i]
            nums[i] = 1
            product = 1
            for j in range(len(nums)):
                product *= nums[j]
            res.append(product)
            nums[i] = hold_original
        return res

            
                
        

# we only want to iterate through the array once
# lets keep track of which element we are pointing to during each iteration and set it to 1. Be sure to save the original value
# so we can reset the array.
# we will loop through the array and multiply all the elements and save that to the result array
# we will reset the index we changed to 1 back to the original
# Loop all of the above

# return the result array