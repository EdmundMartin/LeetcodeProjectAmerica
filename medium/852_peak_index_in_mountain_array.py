from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        for idx in range(1, len(arr) - 1):
            if arr[idx - 1] < arr[idx] and arr[idx + 1] < arr[idx]:
                return idx
