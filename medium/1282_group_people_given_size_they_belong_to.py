from typing import List
from collections import defaultdict


# 64ms - Beats 94.83% of users with Python3
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        sizes = defaultdict(list)

        for idx, size in enumerate(groupSizes):
            sizes[size].append(idx)

        result = []
        for key in sorted(sizes.keys()):
            people = sizes[key]
            while people:
                add, people = people[:key], people[key:]
                result.append(add)
        return result