from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for_majority = len(nums) / 2

        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1
            if seen[num] > for_majority:
                return num
        return -1
