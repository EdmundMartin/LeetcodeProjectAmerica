from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev_price = prices[0]
        total_profit = 0
        for price in prices[1:]:
            if price > prev_price:
                total_profit += price - prev_price
            prev_price = price
        return total_profit


if __name__ == '__main__':
    res = Solution().maxProfit([7,1,5,3,6,4])
    print(res)

    res = Solution().maxProfit([1,2,3,4,5])
    print(res)

    res = Solution().maxProfit([7,6,4,3,1])
    print(res)