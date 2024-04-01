from typing import List


# 40ms - Beats 99.28% of users with Python3
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        for i in range(1, len(mountain) - 1):

            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks
