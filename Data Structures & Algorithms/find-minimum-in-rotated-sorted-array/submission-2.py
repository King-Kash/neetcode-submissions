class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = (right + left) // 2

        min_val = nums[mid]
        while left <= right:
            if nums[left] >= nums[right]: 
                '''Indicates a reordeing must have happened'''
                print(nums[mid])
                if nums[mid] < min_val:
                    min_val = nums[mid]

                if nums[mid] >= nums[left]:
                    '''
                    left half is ordered and m belongs to left. smaller vals must 
                    be on the right since a reording took place.
                    '''
                    left = mid + 1
                    mid = (right + left) // 2
                else:
                    '''
                    everything right of mid must be increasing order if mid < left. 
                    all vals to the right of mid will be larger than mid, so look in the left
                    hald for a possibly smaller value.
                    '''
                    right = mid - 1
                    mid = (right + left) // 2
            else:
                return min(nums[left], min_val)
        
        return min_val
