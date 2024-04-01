from typing import List
from heapq import heapify, heappop


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapify(nums)
        result = []
        while len(nums) > 0:
            alice = heappop(nums)

            if len(nums) == 0:
                result.append(alice)
            else:
                bob = heappop(nums)
                result.extend([bob, alice])
        return result
