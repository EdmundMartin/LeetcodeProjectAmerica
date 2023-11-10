from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = set()
        unique = set()
        for num in nums:
            if num in seen:
                if num in unique:
                    unique.remove(num)
                continue
            unique.add(num)
            seen.add(num)
        return sum(unique)


if __name__ == '__main__':
    res = Solution().sumOfUnique([1, 2, 3, 2])
    print(res)

    res = Solution().sumOfUnique([1, 1, 1, 1])
    print(res)

    res = Solution().sumOfUnique([1, 2, 3, 4, 5])
    print(res)