

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        ending = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in ending:
                if len(stack) == 0:
                    return False
                if stack[-1] == ending[char]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(char)
        return len(stack) == 0