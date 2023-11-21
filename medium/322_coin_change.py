from typing import List


def recursive_solution(choices, total, target, steps):

    current_min = float('inf')
    for choice in choices:
        if choice + total > target:
            continue
        if choice + total == target:
            current_min = min(steps, current_min)
        else:
            current_min = min(current_min, recursive_solution(choices, total + choice, target, steps + 1))
    return current_min


class SolutionToSlow:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        val = recursive_solution(coins, 0, amount, 1)
        if val == float('inf'):
            return -1
        return val


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for cash_amount in range(1, amount + 1):
            for coin in coins:
                if cash_amount - coin >= 0:
                    dp[cash_amount] = min(dp[cash_amount], 1 + dp[cash_amount - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1



if __name__ == '__main__':
    res = Solution().coinChange([1, 2, 5], 11)
    print(res)

    res = Solution().coinChange([2], 3)
    print(res)
