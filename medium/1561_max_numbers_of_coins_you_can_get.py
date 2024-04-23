from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        answer = 0
        i = 0
        j = len(piles)
        while i < j:
            i += 1
            answer += piles[i]
            i += 1
            j -= 1
        return answer
