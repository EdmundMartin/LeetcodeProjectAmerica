from typing import List
from collections import defaultdict


def trim_punc(s: str) -> str:
    if not s[0].isalpha():
        s = s[1:]
    if not s[-1].isalpha():
        s = s[:-1]
    return s.lower()


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        max_val = float('-inf')
        most_common = ""
        counter = defaultdict(int)
        paragraph = paragraph.replace(",", " ")
        for word in paragraph.split(" "):
            if word == " ":
                continue
            w = trim_punc(word)
            if w in banned:
                continue
            counter[w] += 1
            if counter[w] > max_val:
                max_val = counter[w]
                most_common = w
        return most_common


if __name__ == '__main__':
    res = Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    print(res)