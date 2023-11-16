

def reverse_number(num: int):
    parts = []

    while num >= 10:
        remainder = num % 10
        num //= 10
        if remainder == 0 and len(parts) == 0:
            continue
        else:
            parts.append(remainder)
    parts.append(num)

    result = 0
    mult = 1
    while parts:
        last = parts.pop()
        result += last * mult
        mult *= 10
    return result


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        original = num
        reverse_one = reverse_number(num)
        return reverse_number(reverse_one) == original




if __name__ == '__main__':
    res = Solution().isSameAfterReversals(526)
    print(res)

    res = Solution().isSameAfterReversals(1800)
    print(res)



