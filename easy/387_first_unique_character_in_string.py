from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = defaultdict(int)
        for ch in s:
            counter[ch] += 1
        for idx, ch in enumerate(s):
            if counter[ch] == 1:
                return idx
        return -1