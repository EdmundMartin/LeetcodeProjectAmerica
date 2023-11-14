from typing import List
from collections import defaultdict

class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        counter = defaultdict(int)
        for rank in ranks:
            counter[rank] += 1
            if counter[rank] == 3:
                return "Three of a Kind"
        max_value = max(counter.values())
        return "Pair" if max_value == 2 else "High Card"