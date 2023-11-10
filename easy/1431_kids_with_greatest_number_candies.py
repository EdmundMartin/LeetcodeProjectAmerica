from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_value = max(candies)
        return [
            True if candy + extraCandies >= max_value else False for candy in candies
        ]


if __name__ == '__main__':
    res = Solution().kidsWithCandies([2,3,5,1,3], 3)
    print(res)

    res = Solution().kidsWithCandies([4,2,1,1,2], 1)
    print(res)