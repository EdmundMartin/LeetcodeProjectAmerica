from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        total = 0
        last_row = 0
        start_idx = len(grid[0]) - 1
        for row in grid:
            count = last_row
            while start_idx >= 0 and row[start_idx] < 0:
                count += 1
                start_idx -= 1
            total += count
            last_row = count
        return total


if __name__ == '__main__':
    res = Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
    print(res)