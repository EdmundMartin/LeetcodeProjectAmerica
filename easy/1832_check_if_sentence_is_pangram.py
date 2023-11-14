from string import ascii_lowercase


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        words = set(ascii_lowercase)
        for char in sentence:
            if char in words:
                words.remove(char)
        return len(words) == 0
