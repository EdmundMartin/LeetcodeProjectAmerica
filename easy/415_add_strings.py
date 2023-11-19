

def add_strings(s1, s2):
    if len(s1) > len(s2):
        longest, shortest = s1, s2
    else:
        longest, shortest = s2, s1

    result = []
    carry = 0
    count_smaller = len(shortest)
    for i in range(count_smaller):
        left, right = longest[-1], shortest[-1]
        shortest = shortest[:-1]
        longest = longest[:-1]

        total = int(left) + int(right) + carry
        if total >= 10:
            result.append(total % 10)
            carry = 1
        else:
            result.append(total)
            carry = 0
    while longest:
        current, longest = longest[-1], longest[:-1]
        total = carry + int(current)
        if total >= 10:
            result.append(total % 10)
            carry = 1
        else:
            result.append(total)
            carry = 0
    if carry:
        result.append(carry)
    return result


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        backwards_string = add_strings(num1, num2)

        total = 0
        mult = 1
        for num in backwards_string:
            total += num * mult
            mult *= 10
        return str(total)


if __name__ == '__main__':
    res = Solution().addStrings("456", "77")
    print(res)