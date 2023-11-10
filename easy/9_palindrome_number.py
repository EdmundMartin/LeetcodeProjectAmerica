

def _split_reserve_num(num: int):

    results = []
    while num >= 10:
        remainder = num % 10
        results.append(remainder)
        num = num // 10
    results.append(num)
    return results == results[::-1]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return _split_reserve_num(x)


if __name__ == '__main__':
    res = Solution().isPalindrome(10)
    print(res)