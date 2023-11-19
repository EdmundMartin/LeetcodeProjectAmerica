

class Solution:
    def reverseVowels(self, s: str) -> str:
        results = []
        vowels = []
        for char in s:
            if char.lower() in {"a", "e", "i", "o", "u"}:
                vowels.append(char)
                results.append("*")
            else:
                results.append(char)
        for idx, r in enumerate(results):
            if r == "*":
                results[idx] = vowels.pop(-1)
        return "".join(results)