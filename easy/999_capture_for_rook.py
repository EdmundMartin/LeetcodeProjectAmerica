from typing import List


def find_rook(board: List[List[str]]):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == "R":
                return row, col


def search_direction(board, start, direction):
    found = False
    row, col = start
    row_d, col_d = direction
    while 0 <= row < len(board) and 0 <= col < len(board):
        if board[row][col] == 'p':
            return True
        if board[row][col] == 'B':
            return False
        row += row_d
        col += col_d
    return found


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:

        rook_position = find_rook(board)

        count = 0
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if search_direction(board, rook_position, direction):
                count += 1
        return count