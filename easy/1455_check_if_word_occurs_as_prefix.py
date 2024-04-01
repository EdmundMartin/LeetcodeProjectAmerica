

# 26ms - Beats 98.02%of users with Python3
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        result = -1
        for idx, word in enumerate(sentence.split(" ")):
            if len(word) < len(searchWord):
                continue
            if word[:len(searchWord)] == searchWord:
                return idx + 1
        return result