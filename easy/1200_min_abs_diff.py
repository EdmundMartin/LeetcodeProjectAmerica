from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        nums = sorted(arr)

        result = []
        smallest_difference = float('inf')
        for idx in range(len(nums) - 1):

            diff = abs(nums[idx] - nums[idx + 1])
            if diff < smallest_difference:
                smallest_difference = diff
                result = [[nums[idx], nums[idx + 1]]]
            elif diff == smallest_difference:
                result.append([nums[idx], nums[idx + 1]])
        return result
