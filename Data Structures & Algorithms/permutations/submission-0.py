class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        current_num = nums[-1]
        res = self.permute(nums[:-1])
        ret = []
        for permutation in res:
            for i in range(len(permutation)+1):
                new_arr = permutation[:]
                new_arr.insert(i, current_num)
                ret.append(new_arr)
        return ret


'''
1. Define the problem
The task is to return all possible permutations of the original set of nums

2. Make the problem strictly smaller
To make the problem strictly smaller we must find the permutations of a smaller list of nums. We can find the permutations of (n-1) numbers.

3. f(nums) returns all the permutations of the numbers in list nums.

4. Base Case
If you hit an empty list return [[]]
If nums only has one element in it return just that element in its own list [[num]]

5. Legal ways to remove a unit of work
We can remove the last number from the list and try to find the permutation of the remaning numbers f(nums-1)

6. recurrance <-- bit complicated
For each of the list in List[List] we get back we will run an additional for loop from i=0 to len(list). We will insert the num we cut out in the
recursive call into every ith position for every list. This generates every permutation possible for j numbers in the list

7. no need to memoize anything since we end up only ever computing a permutation for j nums once before passing it up to the recursive caller.


'''