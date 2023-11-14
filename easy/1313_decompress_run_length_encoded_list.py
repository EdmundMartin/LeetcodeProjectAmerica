from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for idx in range(0, len(nums), 2):
            freq = nums[idx]
            val = nums[idx + 1]
            result.extend([
                val for _ in range(freq)
            ])
        return result