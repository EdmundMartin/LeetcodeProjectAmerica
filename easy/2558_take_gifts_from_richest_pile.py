from typing import List
from math import sqrt


def largest_pile(items: List[int]):
    max_pile = float('-inf')
    max_idx = -1
    for idx, val in enumerate(items):
        if val > max_pile:
            max_pile = val
            max_idx = idx
    return max_idx


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            idx = largest_pile(gifts)
            output = int(sqrt(gifts[idx]))
            gifts[idx] = output
        return sum(gifts)


if __name__ == '__main__':
    test_data = [25, 64, 9, 4, 100]
    result = Solution().pickGifts(test_data, 4)
    print(result)