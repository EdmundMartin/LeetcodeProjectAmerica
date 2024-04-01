from typing import List
from collections import defaultdict


class SolutionToSlow:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        result = 0
        idx = 0
        while idx < len(nums):

            count_nums = defaultdict(int)

            copy_idx = idx
            count = 0

            if len(nums) - copy_idx <= result:
                return result

            while copy_idx < len(nums):

                count_nums[nums[copy_idx]] += 1

                if count_nums[nums[copy_idx]] > k:
                    break
                count += 1
                copy_idx += 1
            result = max(count, result)
            if copy_idx > idx + 1:
                idx = copy_idx - 1
            else:
                idx += 1
        return result


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)

        result = 0
        idx = 0
        for j in range(len(nums)):
            counter[nums[j]] += 1
            while counter[nums[j]] > k:
                counter[nums[idx]] -= 1
                idx += 1
            result = max(result, j - idx + 1)
        return result