from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_purchase = prices[0]
        max_profit = float('-inf')
        for price in prices[1:]:
            profit = price - min_purchase
            max_profit = max(profit, max_profit)
            min_purchase = min(price, min_purchase)
        return max_profit if max_profit > 0 else 0


if __name__ == '__main__':
    prof = Solution().maxProfit([7,1,5,3,6,4])
    print(prof)

    prof = Solution().maxProfit([7,6,4,3,1])
    print(prof)