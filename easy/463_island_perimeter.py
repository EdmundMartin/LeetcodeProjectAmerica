from typing import List


def check_neighbors(row, col, grid):
    perim = 0
    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for neighbor in neighbors:
        new_row, new_col = row + neighbor[0], col + neighbor[1]
        if new_row < 0 or new_row >= len(grid):
            perim += 1
            continue
        if new_col < 0 or new_col >= len(grid[0]):
            perim += 1
            continue
        if grid[new_row][new_col] == 0:
            perim += 1
    return perim


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        size = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    size += check_neighbors(row, col, grid)
        return size


if __name__ == '__main__':
    g = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    res = Solution().islandPerimeter(g)
    print(res)