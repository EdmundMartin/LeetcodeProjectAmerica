from typing import List


# 34ms Beats 96.89% of users with Python3
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        words = sorted(words, key=len)

        result = []
        for idx in range(len(words)):
            for other_idx in range(idx + 1, len(words)):
                if words[idx] in words[other_idx]:
                    result.append(words[idx])
                    break
        return result