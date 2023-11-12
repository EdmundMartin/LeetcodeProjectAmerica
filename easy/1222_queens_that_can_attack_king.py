from typing import List


def search_from_king(king, direction, queens):
    queue = [(king[0] + direction[0], king[1] + direction[1])]
    while queue:
        row, col = queue.pop(0)
        if (row, col) in queens:
            return [row, col]
        if row < 0 or row >= 8:
            return None
        if col < 0 or col >= 8:
            return None
        queue.append((row + direction[0], col + direction[1]))
    return None


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:

        queen_set = set()
        for queen in queens:
            queen_set.add((queen[0], queen[1]))
        found = []
        for direction in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            attack = search_from_king(king, direction, queen_set)
            if attack:
                found.append(attack)
        return found


if __name__ == '__main__':
    test_queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]]
    test_king = [0, 0]
    res = Solution().queensAttacktheKing(test_queens, test_king)
    print(res)