from typing import List, Set


def compare_rows(word: str, row: Set):
    return all([
        ch.lower() in row for ch in word
    ])


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first, second, third = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        result = []
        for word in words:
            if any([compare_rows(word, r) for r in [first, second, third]]):
                result.append(word)
        return result
