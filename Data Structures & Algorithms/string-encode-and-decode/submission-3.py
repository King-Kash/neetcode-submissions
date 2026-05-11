class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encoded += str(length) + "," + word
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        output = []
        current = 0
        while current < len(s):
            length = ''
            i = current
            while s[i] != ",":
                length += s[i]
                i+=1
            current = i + 1
            length = int(length)
            end = (current+length)
            word = s[current:end]
            output.append(word)
            current = end
        return output

