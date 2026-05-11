class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = defaultdict(list)
        for word in strs:
            print(word)
            char_array = [0] * 26
            for char in word:
                idx = ord(char) - 97
                char_array[idx] += 1
            char_array = tuple(char_array)
            res_dict[char_array].append(word)
        return list(res_dict.values())