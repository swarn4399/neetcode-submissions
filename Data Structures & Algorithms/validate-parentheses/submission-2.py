class Solution:
    def isValid(self, s: str) -> bool:
        dict_s = {")":"(", "}":"{", "]":"["}
        stack = []
        if len(s) == 1:
            return False
        for char in s:
            if stack and char in dict_s:
                if stack[-1] != dict_s[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        if stack:
            return False
        return True