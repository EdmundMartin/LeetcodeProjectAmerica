from typing import List


class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:

        number_teams = len(grid)

        for idx in range(number_teams):
            if sum(grid[idx]) == number_teams - 1:
                return idx
