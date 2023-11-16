from string import ascii_lowercase, ascii_uppercase


class Solution:
    def toLowerCase(self, s: str) -> str:
        mapping = {}
        for lower, upper in zip(ascii_lowercase, ascii_uppercase):
            mapping[upper] = lower

        result = ""
        for ch in s:
            if ch in mapping:
                result += mapping[ch]
            else:
                result += ch
        return result