from typing import List


def search_and_mark(row, col, grid):

    queue = [(row, col)]
    directions = [
        (0, 1), (1, 0), (0, -1), (-1, 0)
    ]
    while queue:
        r, c = queue.pop()
        if grid[r][c] == "X":
            grid[r][c] = "."
        for dir in directions:
            new_r, new_c = r + dir[0], c + dir[1]
            if new_r < 0 or new_r >= len(grid):
                continue
            if new_c < 0 or new_c >= len(grid[0]):
                continue
            if grid[new_r][new_c] == "X":
                queue.append((new_r, new_c))


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "X":
                    count += 1
                    search_and_mark(row, col, board)
        return count
