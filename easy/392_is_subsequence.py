

# 33ms - Beats 90.39% of users with Python3
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        idx = 0
        for ch in t:
            if ch == s[idx]:
                idx += 1
            if idx == len(s):
                return True
        return len(s) == idx
