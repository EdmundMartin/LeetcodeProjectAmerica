from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        expected = sorted(heights)
        idx = 0
        count = 0
        while idx < len(heights):
            if heights[idx] != expected[idx]:
                count += 1
            idx += 1
        return count
