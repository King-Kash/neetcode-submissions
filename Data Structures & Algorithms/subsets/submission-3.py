class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
            The recursion is as follows: For each call of subsets[nums] we want to find all the subsets that must contain the last element and
            append them to the return of the recursive call which will give us all the subsets that must contain the second to last element
            but nothing beyond it.
            To find all the subsets that contain the last element we need to take all the subsets from the recursive call and simply append
            the last element of nums to them. Then we take these new subsets and include alongside the subsets not including the last element
            that we got from the recursive call.

            Algorithim
            all_subsets = []
            1. Begin with the base case []. The only subset we can make with the empty set is []. all_subsets = [[]]
            2. Next we have [1]. All the subsets that must contain 1 can be found by taking all the subsets from the empty set and 
            appending 1 to them. [1] -> [] + 1 -> [1]. Then add this new subset to the list of subsets we have already found which
            we are storing in all_subsets. all_subsets = [[], [1]]
            3. Repeat what we did in step 2 all the way till the full nums array. 
                [1,2]: The recursive call to subsets([1]) returns [[], [1]]. To each of these we add 2 and we get: [2], [1,2].
                Now we include these two new subsets in our collection of all subarrays. all_subarrays = [[], [1], [2], [1,2]]

                [1,2,3]: The recurssive call to subsets([1,2]) returns [[], [1], [2], [1,2]] to each of these we add 3.
                [[3], [1,3], [2,3], [1,2,3]]. We include these new subsets in our collection of all subarrays.
                all_subarrays = [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

            NOTE: THIS MUST BE ACHIVED RECURSIVELY!
        '''
        if not nums:
            return [[]]
        
        current_num = nums[-1]

        res = self.subsets(nums[:-1])
        ret = []

        for subset in res:
            new_array = subset[:]
            new_array += [current_num]
            ret.append(new_array)
            ret.append(subset)
        return ret
        
