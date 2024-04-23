from typing import List


def split_integer(num: int) -> int:
    nums = []
    while num >= 10:
        remainder = num % 10
        num //= 10
        nums.append(remainder)
    nums.append(num)
    max_num = max(nums)

    mult = 1
    result = 0
    while nums:
        nums.pop()
        result += max_num * mult
        mult *= 10
    return result


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum([
          split_integer(num) for num in nums
        ])