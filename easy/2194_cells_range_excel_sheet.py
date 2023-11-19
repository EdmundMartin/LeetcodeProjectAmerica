from typing import List


from string import ascii_uppercase


class Solution:
    def cellsInRange(self, s: str) -> List[str]:

        start_idx, end_idx = ascii_uppercase.index(s[0]), ascii_uppercase.index(s[3])

        start_num, end_num = int(s[1]), int(s[4])

        result = []
        for idx in range(start_idx, end_idx + 1):
            letter = ascii_uppercase[idx]
            for num in range(start_num, end_num + 1):
                result.append(
                    f"{letter}{num}"
                )
        return result
