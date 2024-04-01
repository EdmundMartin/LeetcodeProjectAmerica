from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_subarray = nums[0]
        current_sum = 0

        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            max_subarray = max(max_subarray, current_sum)
        return max_subarray

