from typing import List


class SolutionSlow:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total = 0
        while len(grid[0]):
            current_max = float('-inf')

            for row in grid:
                row_max = float('-inf')
                for value in row:
                    if value > current_max:
                        current_max = value
                    if value > row_max:
                        row_max = value
                row.remove(row_max)
            total += current_max
        return total


# 89ms - Beats 92.10% of users with Python3
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        new_grid = []
        for row in grid:
            new_grid.append(sorted(row))
        idx = len(new_grid[0]) - 1
        total = 0
        while idx >= 0:
            current_max = float('-inf')
            for row in new_grid:
                current_max = max(current_max, row[idx])
            idx -= 1
            total += current_max
        return total


if __name__ == '__main__':
    res = Solution().deleteGreatestValue([[1,2,4],[3,3,1]])
    print(res)