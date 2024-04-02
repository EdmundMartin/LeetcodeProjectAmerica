from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        unique_one = set(nums1)
        unique_two = set(nums2)

        result_one = []
        result_two = []

        for num in unique_one:
            if num not in unique_two:
                result_one.append(num)
        for num in unique_two:
            if num not in unique_one:
                result_two.append(num)

        return [
            result_one, result_two
        ]