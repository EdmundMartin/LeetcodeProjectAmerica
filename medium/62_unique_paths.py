

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [

        ]
        for row in range(m):
            result.append([0] * n)
        result[m - 1][n - 1] = 1

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    continue
                total = 0
                if col < n - 1:
                    total += result[row][col + 1]
                if row < m - 1:
                    total += result[row + 1][col]
                result[row][col] = total
        return result[0][0]


if __name__ == '__main__':
    Solution().uniquePaths(3, 7)