class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for c in s:
                index = ord(c) - ord('a') + 1
                counts[index]  += 1
            key = tuple(counts)
            anagrams[key].append(s)
        return list(anagrams.values())