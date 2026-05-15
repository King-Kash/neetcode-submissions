class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_of_squares(current):
            new_num = 0
            while current > 0:
                new_num += (current%10)**2
                current //= 10
            return new_num
        
        slow = n
        fast = sum_of_squares(n)
        
        while True:
            slow = sum_of_squares(slow)
            fast = sum_of_squares(sum_of_squares(fast))
            if slow == fast:
                if fast == 1:
                    return True
                else:
                    return False
