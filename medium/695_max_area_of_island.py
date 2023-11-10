from typing import List


def search_neighbors(row, col, grid):
    seen = set()
    seen.add((row, col))

    area = 1
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    queue = [(row, col)]
    while queue:
        r, c = queue.pop(0)
        for dir in directions:
            new_r, new_c = r + dir[0], c + dir[1]
            if (new_r, new_c) in seen:
                continue
            seen.add((new_r, new_c))
            if new_r < 0 or new_r >= len(grid):
                continue
            if new_c < 0 or new_c >= len(grid[0]):
                continue
            if grid[new_r][new_c] == 1:
                area += 1
                grid[new_r][new_c] = 0
                queue.append((new_r, new_c))
    return area


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res = search_neighbors(row, col, grid)
                    max_area = max(max_area, res)
        return max_area


if __name__ == '__main__':
    test_grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    res = Solution().maxAreaOfIsland(test_grid)
    print(res)