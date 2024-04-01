from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:

        result = []
        for word in words:
            for sub_word in word.split(separator):
                if len(sub_word) > 0:
                    result.append(sub_word)
        return result
