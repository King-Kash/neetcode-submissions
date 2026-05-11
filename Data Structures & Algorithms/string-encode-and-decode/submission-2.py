class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encoded += str(length) + word
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        output = []
        current = 0
        while current < len(s):
            length = int(s[current])
            current += 1
            end = (current+length)
            word = s[current:end]
            output.append(word)
            current = end
        return output

