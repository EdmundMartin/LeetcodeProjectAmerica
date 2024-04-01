from typing import List


def multiply(nums: List[int], start: int, end: int):
    if start > end or end < start:
        return 1
    total = nums[start]
    start += 1
    for idx in range(start, end + 1):
        total *= nums[idx]
    return total


class SolutionToSlow:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        post_fix = [1] * len(nums)
        pre_fix = [1] * len(nums)

        for idx in range(len(nums)):
            post_fix[idx] = multiply(nums, idx + 1, len(nums) - 1)
            pre_fix[idx] = multiply(nums, 0, idx - 1)

        result = []
        for idx in range(len(nums)):
            result.append(pre_fix[idx] * post_fix[idx])
        return result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix = 1
        for idx in range(len(nums)):
            result[idx] = prefix
            prefix *= nums[idx]

        postfix = 1
        for idx in range(len(nums) - 1, -1, -1):
            result[idx] *= postfix
            postfix *= nums[idx]
        return result



if __name__ == '__main__':
    res = multiply([1, 2, 3], 0, 2)
    print(res)

    res = SolutionToSlow().productExceptSelf([1, 2, 3, 4])
    print(res)