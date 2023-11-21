from typing import List


# 150ms - Beats 94.16% of users with Python3
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        in_one = dict()
        in_two = dict()

        for idx, word in enumerate(list1):
            if word in in_one:
                continue
            in_one[word] = idx
        for idx, word in enumerate(list2):
            if word in in_two:
                continue
            in_two[word] = idx

        min_sum = float('inf')
        result = [

        ]
        for candidate, idx in in_one.items():
            if candidate in in_two:
                total = idx + in_two[candidate]
                if total < min_sum:
                    result = [candidate]
                    min_sum = total
                elif total == min_sum:
                    result.append(candidate)
        return result
