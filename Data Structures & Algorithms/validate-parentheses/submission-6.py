class Solution:
    def isValid(self, s: str) -> bool:
        if len(opening) % 2 != 0:
            return False
        opening = []
        for paren in s:
            if paren == '{' or paren == '[' or paren == '(':
                opening.append(paren)
            else:
                match paren:
                    case '}':
                        partner = opening.pop()
                        if partner != '{':
                            return False
                    case ']':
                        partner = opening.pop()
                        if partner != '[':
                            return False
                    case ')':
                        partner = opening.pop()
                        if partner != '(':
                            return False
                    case _:
                        return False
        if len(opening) != 0:
            return False
        return True
        