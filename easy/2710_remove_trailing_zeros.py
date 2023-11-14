

# 35ms - Beats 96.33 %of users with Python3
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        idx = len(num) - 1
        while num[idx] == "0":
            idx -= 1
        return num[:idx + 1]


if __name__ == '__main__':
    res = Solution().removeTrailingZeros("51230100")
    print(res)