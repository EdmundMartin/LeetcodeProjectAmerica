from typing import List
from collections import defaultdict


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        mapping = defaultdict(list)
        for path in paths:
            start, end = path
            mapping[start].append(end)
            if end not in mapping:
                mapping[end] = []
        for key, val in mapping.items():
            if len(val) == 0:
                return key