from string import ascii_lowercase


class Solution:
    def replaceDigits(self, s: str) -> str:
        char_to_idx = {}
        idx_to_char = {}
        for idx, char in enumerate(ascii_lowercase):
            char_to_idx[char] = idx
            idx_to_char[idx] = char

        result = ""
        for idx, char in enumerate(s):
            if char.isalpha():
                result += char
            else:
                last = s[idx - 1]
                next_idx = char_to_idx[last]
                next_idx = next_idx + int(char)
                result += idx_to_char[next_idx]
        return result
