from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] >= len(nums):
            return True

        can_make_it = [False] * len(nums)

        for idx in range(len(nums) - 1, -1, -1):
            current_jump = nums[idx]
            if idx + current_jump >= len(nums) - 1:
                can_make_it[idx] = True
            for option in range(current_jump + 1):
                next_idx = idx + option
                if next_idx < len(nums) and can_make_it[next_idx] is True:
                    can_make_it[idx] = True
                    break
        return can_make_it[0]


if __name__ == '__main__':
    res = Solution().canJump([2, 3, 1, 1, 4])
    print(res)