from string import ascii_lowercase


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        row, col = coordinates[0], int(coordinates[1])

        row = ascii_lowercase.index(row) + 1
        if row % 2 == 0 and col % 2 != 0:
            return True
        if row % 2 != 0 and col % 2 == 0:
            return True
        return False


if __name__ == '__main__':
    res = Solution().squareIsWhite("a2")
    print(res)

    res = Solution().squareIsWhite("h3")
    print(res)

    res = Solution().squareIsWhite("c7")
    print(res)