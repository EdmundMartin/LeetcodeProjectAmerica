

class Solution:
    def checkString(self, s: str) -> bool:
        seen_b = False

        for char in s:
            if char == "b":
                seen_b = True
            if char != "b" and seen_b:
                return False
        return True
