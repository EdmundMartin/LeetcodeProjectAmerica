from typing import List


def is_even_digit(num: int):
    count = 1
    while num >= 10:
        num /= 10
        count += 1
    return count % 2 == 0


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if is_even_digit(num):
                count += 1
        return count