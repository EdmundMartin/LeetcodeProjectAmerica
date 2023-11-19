from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for idx in range(1, len(nums)):
            if nums[i] != nums[idx]:
                i += 1
                nums[i] = nums[idx]
        return i + 1


if __name__ == '__main__':
    res = Solution().removeDuplicates([1, 1, 2])
    print(res)

    res = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(res)