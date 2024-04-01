from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1

        for char in t:
            if char not in counter:
                return char
            counter[char] -= 1
            if counter[char] < 0:
                return char
