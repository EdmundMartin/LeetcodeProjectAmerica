from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        first = 0
        count = 0
        while first < len(nums) - 1:
            for idx in range(first + 1, len(nums)):
                if nums[first] + nums[idx] < target:
                    count += 1
            first += 1
        return count