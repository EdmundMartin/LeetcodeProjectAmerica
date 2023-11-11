from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True

        seen_decrease = False
        seen_increase = False
        for idx in range(1, len(nums)):

            if nums[idx] < nums[idx -1]:
                seen_decrease = True
            if nums[idx] > nums[idx - 1]:
                seen_increase = True
            if seen_increase and seen_decrease:
                return False
        return True


if __name__ == '__main__':
    res = Solution().isMonotonic([1, 2, 2, 3])
    print(res)

    res = Solution().isMonotonic([6, 5, 4, 4])
    print(res)

    res = Solution().isMonotonic([1, 3, 2])
    print(res)