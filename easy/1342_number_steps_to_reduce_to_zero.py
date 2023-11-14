

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        return steps


if __name__ == '__main__':
    res = Solution().numberOfSteps(14)
    print(res)

    res = Solution().numberOfSteps(8)
    print(res)

    res = Solution().numberOfSteps(123)
    print(res)