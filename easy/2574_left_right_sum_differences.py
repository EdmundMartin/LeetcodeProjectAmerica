from typing import List


class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        left_sum = [0 for _ in range(len(nums))]
        running_total = 0
        for idx in range(1, len(nums)):
            left_sum[idx] = nums[idx - 1] + running_total
            running_total = left_sum[idx]

        right_sum = [0 for _ in range(len(nums))]
        running_total = 0
        for idx in range(len(nums) - 2, -1, -1):
            right_sum[idx] = nums[idx + 1] + running_total
            running_total = right_sum[idx]

        return [
            abs(x - y) for x, y in zip(left_sum, right_sum)
        ]


if __name__ == '__main__':
    Solution().leftRightDifference([10, 4, 8, 3])