class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = ''.join(sorted(s))
        sortedT = ''.join(sorted(t))

        if hash(sortedS) == hash(sortedT):
            return True
        return False
        