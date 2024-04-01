from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            left, right = idx + 1, len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + val
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([val, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result