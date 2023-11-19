

def compare(haystack, needle):
    if needle > haystack:
        return False
    idx = 0
    for char in needle:
        if char != haystack[idx]:
            return False
        idx += 1
    return True


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        for idx, char in enumerate(haystack):
            if char == needle[0]:
                if compare(haystack[idx:], needle):
                    return idx
        return -1