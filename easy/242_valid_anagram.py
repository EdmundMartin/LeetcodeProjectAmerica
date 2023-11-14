from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1
        for char in t:
            if char not in counter:
                return False
            if counter[char] == 0:
                return False
            counter[char] -= 1
        return True