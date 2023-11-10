

class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for char in s.lower():
            if char.isalpha() or char.isalnum():
                result = result + char
        return result == result[::-1]