from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = set()
        seen_twice = set()

        for num in nums:
            if num not in seen_once:
                seen_once.add(num)
            elif num in seen_once:
                seen_twice.add(num)
        result = seen_once.difference(seen_twice)
        return list(result)[0]


if __name__ == '__main__':
    res = Solution().singleNumber([2, 2, 1])
    print(res)
