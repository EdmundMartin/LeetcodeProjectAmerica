from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                temp = abs(nums[i] - nums[i-1]) + 1
                nums[i] += temp
                count += temp
        return count


if __name__ == '__main__':
    res = Solution().minOperations([1, 1, 1])
    print(res)

    res = Solution().minOperations([1, 5, 2, 4, 1])
    print(res)
