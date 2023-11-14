from typing import List

from collections import defaultdict


def to_word_dict(sentence: str):
    result = defaultdict(int)
    for word in sentence.split(" "):
        result[word] += 1
    return result


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        results = []
        sentence_one = to_word_dict(s1)
        sentence_two = to_word_dict(s2)

        for word, count in sentence_one.items():
            if count == 1 and word not in sentence_two:
                results.append(word)
        for word, count in sentence_two.items():
            if count == 1 and word not in sentence_one:
                results.append(word)
        return results