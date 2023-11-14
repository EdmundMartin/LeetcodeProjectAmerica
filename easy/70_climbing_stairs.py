

def recursive_solve(n: int, seen) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in seen:
        return seen[n]
    one_step = recursive_solve(n - 1, seen)
    seen[n - 1] = one_step

    two_step = recursive_solve(n - 2, seen)
    seen[n - 2] = two_step
    return one_step + two_step


class Solution:
    def climbStairs(self, n: int) -> int:
        return recursive_solve(n, dict())


if __name__ == '__main__':
    res = Solution().climbStairs(3)
    print(res)