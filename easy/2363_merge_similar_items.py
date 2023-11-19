from typing import List
from collections import defaultdict


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        all_items = defaultdict(int)

        for item in items1:
            all_items[item[0]] += item[1]
        for item in items2:
            all_items[item[0]] += item[1]

        result = sorted([
            [k, v] for k, v in all_items.items()
        ])
        return result