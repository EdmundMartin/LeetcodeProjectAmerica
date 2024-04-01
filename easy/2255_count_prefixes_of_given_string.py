from typing import List


# 56ms - Beats 93.73% of users with Python3
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for prefix in words:
            if len(prefix) > len(s):
                continue
            if s[:len(prefix)] == prefix:
                count += 1
        return count
