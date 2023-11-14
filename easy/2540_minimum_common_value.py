from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set_one = set()
        set_two = set()

        for num1 in nums1:
            set_one.add(num1)
        for num2 in nums2:
            set_two.add(num2)

        intersect = set_one.intersection(set_two)
        if len(intersect) == 0:
            return -1
        if len(intersect) == 1:
            return list(intersect)[0]
        return min(intersect)


if __name__ == '__main__':
    res = Solution().getCommon([1, 2, 3], [2, 4])
    print(res)