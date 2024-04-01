from collections import defaultdict


# 33ms - Beats 91.23% of users with Python3
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word_one_counter = defaultdict(int)
        word_two_counter = defaultdict(int)

        for char in word1:
            word_one_counter[char] += 1
            word_two_counter[char] += 0
        for char in word2:
            word_two_counter[char] += 1
            word_one_counter[char] += 0

        for char in word_one_counter.keys():
            diff = abs(word_one_counter[char] - word_two_counter[char])
            if diff > 3:
                return False
        return True