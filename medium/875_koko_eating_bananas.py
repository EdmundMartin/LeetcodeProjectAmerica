from typing import List
import math


def calculate_time(piles: List[int], k: int):
    hours = 0
    for pile in piles:
        count = math.ceil(pile / k)
        hours += count
    return hours


# 282ms - Beats 96.91% of users with Python3
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        result = right
        while left <= right:
            middle = (left + right) // 2
            hours = calculate_time(piles, middle)

            if hours > h:
                left = middle + 1
            else:
                result = min(middle, result)
                right = middle - 1
        return result


if __name__ == '__main__':
    res = Solution().minEatingSpeed([3, 6, 7, 11], 8)
    print(res)