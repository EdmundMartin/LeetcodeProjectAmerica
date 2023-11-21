from typing import List
from string import ascii_lowercase


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        mapping = {}
        for idx, ch in enumerate(ascii_lowercase):
            mapping[ch] = idx
        current_row = 0
        rows = 0
        for ch in s:
            idx = mapping[ch]
            current_width = widths[idx]

            if current_row + current_width <= 100:
                current_row += current_width
            else:
                rows += 1
                current_row = current_width

        if current_row > 0:
            rows += 1
        return [rows, current_row]


if __name__ == '__main__':
    test_widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    test_s = "bbbcccdddaaa"

    res = Solution().numberOfLines(test_widths, test_s)
    print(res)