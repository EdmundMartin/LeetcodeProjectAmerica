from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        nums = dict()
        for idx, num in enumerate(arr):
            nums[num] = idx
        for idx, num in enumerate(arr):
            if num % 2 != 0:
                continue
            if num // 2 in nums:
                if nums[num // 2] != idx:
                    return True
        return False


if __name__ == '__main__':
    Solution().checkIfExist([10, 2, 5, 3])