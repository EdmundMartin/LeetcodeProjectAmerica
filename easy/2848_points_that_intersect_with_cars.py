from typing import List


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = set()

        for num in nums:
            for item in range(num[0], num[1] + 1):
                points.add(item)
        return len(points)


if __name__ == '__main__':
    res = Solution().numberOfPoints([[3,6],[1,5],[4,7]])
    print(res)

    res = Solution().numberOfPoints([[1,3],[5,8]])
    print(res)
