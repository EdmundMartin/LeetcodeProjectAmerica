from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = float('-inf')
        for account in accounts:
            max_wealth = max(sum(account), max_wealth)
        return max_wealth
