from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            if len(word) < len(pref):
                continue
            if word[:len(pref)] == pref:
                count += 1
        return count

