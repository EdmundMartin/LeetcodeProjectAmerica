from typing import List


# 368ms - Beats 95.03% of users with Python3
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        largest = 0
        for num in nums:
            if num - 1 in nums:
                continue
            current_num = num
            count = 0
            while current_num in nums:
                current_num += 1
                count += 1
            largest = max(largest, count)
        return largest


if __name__ == '__main__':
    res = Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
    print(res)