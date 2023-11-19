from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        count = 0
        for idx in range(len(nums)):
            for other_idx in range(idx + 1, len(nums)):
                if nums[idx] == nums[other_idx]:
                    count += 1
        return count