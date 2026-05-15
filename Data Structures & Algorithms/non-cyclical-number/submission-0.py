class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        current = n
        while True:
            new_num = 0
            while current > 0:
                new_num += (current%10)**2
                current //= 10
            if new_num in seen:
                return False
            if new_num == 1:
                return True
            current = new_num
            seen.add(new_num)
