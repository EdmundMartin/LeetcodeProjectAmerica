from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        prev = 0
        total = 0
        for bracket in brackets:
            end, rate = bracket
            to_pay = min(income, end) - prev
            if to_pay < 0:
                break
            total += (to_pay / 100) * rate
            prev = end
        return total


if __name__ == '__main__':
    result = Solution().calculateTax([[3,50],[7,10],[12,25]], 10)
    print(result)

    result = Solution().calculateTax([[1,0],[4,25],[5,50]], 2)
    print(result)