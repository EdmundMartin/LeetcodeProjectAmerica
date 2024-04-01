from typing import List


def recursive_solve(prices: List[int],  idx: int, cost: int):
    total_cost = 0 + cost
    if idx >= len(prices):
        return total_cost

    total_cost += prices[idx]

    next_idx = (idx + 1) * 2
    if idx == 0:
        next_idx = 2

    result = float('inf')
    for i in range(idx + 1, next_idx + 1):
        res = recursive_solve(prices, i, total_cost)
        result = min(res, result)
    return result


class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        return recursive_solve(prices, 0, 0)