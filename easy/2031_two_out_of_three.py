from typing import List

from collections import defaultdict


def count_items(counter, items: List[int]):
    seen = set()
    for item in items:
        if item not in seen:
            counter[item] += 1
        seen.add(item)


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        counter = defaultdict(int)

        for arr in [nums1, nums2, nums3]:
            count_items(counter, arr)
        return [
            k for k, v in counter.items() if v >= 2
        ]