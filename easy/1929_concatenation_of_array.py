from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [None] * (len(nums) * 2)

        for idx, num in enumerate(nums):
            result[idx] = num
            result[idx + len(nums)] = num
        return result