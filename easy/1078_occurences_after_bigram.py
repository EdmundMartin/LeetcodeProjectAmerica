from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:

        seen = []
        result = []
        for word in text.split(" "):
            if len(seen) >= 2:
                if seen[-2] == first and seen[-1] == second:
                    result.append(word)
            seen.append(word)
        return result