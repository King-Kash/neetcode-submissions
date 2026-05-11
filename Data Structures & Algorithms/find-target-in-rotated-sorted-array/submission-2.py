class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        mid = (right + left) // 2

        while left <= right:
            if target == nums[mid]:
                return mid
            
            if nums[right] < nums[left]:
                #the list has been reordered
                if nums[left] <= nums[mid]:
                    '''above must be <= ex([3,1] where left and mid are both the same)'''
                    #left half is gaurenteed to be ordered
                    if target < nums[mid] and target >= nums[left]:
                        #target may be in the left half, search that half
                        right = mid - 1
                        mid = (right + left) // 2
                    else:
                        #target may be in right half
                        left = mid + 1
                        mid = (right + left) // 2
                else:
                    #right half is gaurenteed to be ordered
                    if target > nums[mid] and target <= nums[right]:
                        left = mid + 1
                        mid = (right + left) // 2
                    else:
                        right = mid - 1
                        mid = (right + left) // 2
            else:
                if target < nums[mid]:
                        right = mid - 1
                        mid = (right + left) // 2
                else:
                        left = mid + 1
                        mid = (right + left) // 2
        
        return -1
