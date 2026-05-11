class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        bigArray = []
        tripletArray = []
        sum = 0
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                sum = nums[i]
                for k in range(j+1, len(nums)):
                    sum = nums[i] + nums[j]
                    sum += nums[k]
                    if sum == 0:
                        tripletArray = [nums[i], nums[j], nums[k]]
                        tripletArray.sort()
                        add = True;
                        for triplet in bigArray:
                                if ( (tripletArray[0] == triplet[0]) and (tripletArray[1] == triplet[1]) and (tripletArray[2] == triplet[2])):
                                   add = False;
                        if add:
                            bigArray.append(tripletArray)            
        return bigArray


        # big return array
        # tiny triplet array

        # for each num in rang len minus 2
        #     add first num to zero
        #     for each num in range of len minus 1
        #         add second num to 1st + 0
        #         for the rest of the numbers
        #             add the third number to the current sum to see if we get 0
        #             if yes
        #                 add them to the triplet array
        #                 check if this triplet is already in the return array
        #                     if no
        #                         add it
        #             if no
        #                 move to the next one
                
        