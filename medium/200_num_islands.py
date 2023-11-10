from typing import List


def set_island_to_zeros(row, col, grid):
    queue = [(row, col)]
    grid[row][col] = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        r, c = queue.pop()
        for dir in directions:
            new_r, new_c = r + dir[0], c + dir[1]
            if new_r < 0 or new_r >= len(grid):
                continue
            if new_c < 0 or new_c >= len(grid[0]):
                continue
            if grid[new_r][new_c] == "1":
                grid[new_r][new_c] = 0
                queue.append((new_r, new_c))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    set_island_to_zeros(row, col, grid)
        return count


if __name__ == '__main__':
    test_grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    res = Solution().numIslands(test_grid)
    print(res)

    test_grid_two = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    res = Solution().numIslands(test_grid_two)
    print(res)