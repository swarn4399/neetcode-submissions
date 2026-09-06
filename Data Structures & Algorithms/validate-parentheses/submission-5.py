class Solution:
    def isValid(self, s: str) -> bool:
        dict_s = {")":"(", "}":"{", "]":"["}
        stack = []
        if len(s) == 1:
            return False
        for char in s:
            if stack and char in dict_s:
                if stack and stack[-1] == dict_s[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True