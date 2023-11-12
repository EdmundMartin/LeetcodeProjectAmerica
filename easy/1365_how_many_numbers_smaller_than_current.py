from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        result = []
        for num in nums:
            idx = sorted_nums.index(num)
            result.append(idx)
        return result


if __name__ == '__main__':
    Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3])