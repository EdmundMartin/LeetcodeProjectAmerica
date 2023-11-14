from typing import List


def recursive_min_cost(costs, idx, cost):
    if idx >= len(costs):
        return cost
    cost += costs[idx]
    results = []
    for option in [idx + 1, idx + 2]:
        results.append(recursive_min_cost(costs, option, cost))
    return min(results)


class SolutionTooSlow:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(
            recursive_min_cost(cost, 0, 0),
            recursive_min_cost(cost, 1, 0)
        )


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costs = [None] * len(cost)
        costs[-1] = cost[-1]
        idx = len(costs) - 2
        while idx >= 0:
            if idx + 2 >= len(cost):
                costs[idx] = cost[idx]
            else:
                costs[idx] = cost[idx]
                costs[idx] += min(costs[idx + 1], costs[idx + 2])
            idx -= 1
        return min(costs[0], costs[1])



if __name__ == '__main__':
    """
    res = Solution().minCostClimbingStairs([10, 15, 20])
    print(res)
    """

    res = Solution().minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
    print(res)