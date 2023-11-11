from typing import List


def split_number(num: int) -> List[int]:
    results = []
    while num >= 10:
        remainder = num % 10
        num = num // 10
        results.append(remainder)
    results.append(num)
    return results


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen and n != 1:
            seen.add(n)
            split_nums = split_number(int(n))
            total = 0
            for num in split_nums:
                total += num * num
            n = total
        return n == 1


if __name__ == '__main__':
    res = Solution().isHappy(19)
    print(res)

    res = Solution().isHappy(2)
    print(res)