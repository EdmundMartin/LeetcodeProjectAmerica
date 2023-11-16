from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = []
        for idx, price in enumerate(prices):
            current_price = price
            for discount in range(idx + 1, len(prices)):
                if prices[discount] <= price:
                    current_price -= prices[discount]
                    break
            result.append(current_price)
        return result


if __name__ == '__main__':
    res = Solution().finalPrices([8, 4, 6, 2, 3])
    print(res)