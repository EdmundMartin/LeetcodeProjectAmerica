from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_val = float('-inf')
        for sentence in sentences:
            split_sentence = len(sentence.split(" "))
            if split_sentence > max_val:
                max_val = split_sentence
        return max_val