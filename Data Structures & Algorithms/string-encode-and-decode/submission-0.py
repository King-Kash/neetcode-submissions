class Solution:
    def __init__(self):
        self.wordLibrary = {}

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for i in range(len(strs)):
            self.wordLibrary[i] = strs[i]
            encodedString += str(i)
        print(encodedString)
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedArray = []
        for char in s:
            key = int(char)
            value = self.wordLibrary[key]
            decodedArray.append(value)
        for element in decodedArray:
            print(element)
        return decodedArray

