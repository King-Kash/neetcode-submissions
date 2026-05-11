class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = defaultdict(List)
        right = 0
        left = 0

        # Phase 1 - Sort s1:
        sorted_s1 = sorted(s1)
        sorted_s1 = "".join(sorted_s1)
        print(sorted_s1)

        if len(s2) < len(s1):
            return False

        # Invariant: The window size must be max length of s1
        for right in range(len(s2)):
            if (right - left + 1) > len(s1):
                left += 1
            substring = s2[left:(right+1)]
            sorted_s2 = sorted(substring)
            sorted_s2 = "".join(sorted_s2)

            if(sorted_s2 == sorted_s1):
                return True
        
        return False
            


        
