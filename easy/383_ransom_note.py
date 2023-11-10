from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        characters = defaultdict(int)
        for char in magazine:
            characters[char] += 1
        for char in ransomNote:
            if char not in characters:
                return False
            characters[char] -= 1
            if characters[char] < 0:
                return False
        return True
