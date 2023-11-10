from typing import List, Dict


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: Dict[int, int] = dict()

        for idx, number in enumerate(nums):
            other = target - number
            if other in seen:
                return [seen[other], idx]
            seen[number] = idx
        return [-1, -1]