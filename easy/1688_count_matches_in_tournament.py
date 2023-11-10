

class Solution:
    def numberOfMatches(self, n: int) -> int:
        if n == 1:
            return 0
        matches = 1
        while n > 2:
            if n % 2 != 0:
                rem = (n - 1) // 2
                matches += rem
            else:
                rem = n // 2
                matches += rem
            n -= rem
        return matches


if __name__ == '__main__':
    res = Solution().numberOfMatches(14)
    print(res)