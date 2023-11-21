from typing import List
from collections import defaultdict


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = defaultdict(int)
        for num in arr:
            counter[num] += 1
        return len(set(counter.keys())) == len(set(counter.values()))