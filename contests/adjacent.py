from string import ascii_lowercase


class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        is_char = set(ascii_lowercase)
        chars = list(word)
        prev = chars[0]
        idx = 1
        count = 0
        while idx < len(word):
            if prev not in is_char:
                pass
            elif abs(ascii_lowercase.index(prev) - ascii_lowercase.index(chars[idx])) <= 1:
                count += 1
                chars[idx] = '?'
            prev = chars[idx]
            idx += 1
        return count