from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        results = []
        for idx, word in enumerate(words):
            if x in word:
                results.append(idx)
        return results
