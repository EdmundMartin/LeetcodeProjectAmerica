


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(" ")

        for idx in range(1, len(words)):
            if words[idx - 1][-1] != words[idx][0]:
                return False
        if words[-1][-1] != words[0][0]:
            return False
        return True