from typing import List


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        sum = 0
        max_num = max(nums)
        while k > 0:
            sum += max_num
            max_num += 1
            k -= 1
        return sum


if __name__ == '__main__':
    res = Solution().maximizeSum([1, 2, 3, 4, 5], 3)
    print(res)