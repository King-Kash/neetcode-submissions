class Solution:
    def __init__(self):
        self.wordLibrary = {}

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for i in range(len(strs)):
            key = str(i)
            self.wordLibrary[key] = strs[i]
            encodedString += key + ","
        return encodedString

    def decode(self, s: str) -> List[str]:
        print(s)
        decodedArray = []
        keyAccumulator = ""
        for i in range(len(s)):
            if s[i] != ",":
                keyAccumulator += s[i]
            else:
                value = self.wordLibrary[keyAccumulator]
                print(value)
                keyAccumulator = ""
                decodedArray.append(value)
        return decodedArray

