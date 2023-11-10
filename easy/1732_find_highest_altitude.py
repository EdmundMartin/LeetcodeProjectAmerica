from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0
        highest = 0
        for el in gain:
            start += el
            highest = max(highest, start)
        return highest


if __name__ == '__main__':
    res = Solution().largestAltitude([-5, 1, 5, 0, -7])
    print(res)