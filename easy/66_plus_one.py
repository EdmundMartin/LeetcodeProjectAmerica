from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        carry = 1
        idx = len(digits) - 1

        while idx >= 0:
            if digits[idx] == 9 and carry:
                digits[idx] = (digits[idx] + carry) % 10
                carry = 1
            else:
                digits[idx] += carry
                carry = 0
            idx -= 1
        if carry:
            return [carry] + digits
        return digits


if __name__ == '__main__':
    res = Solution().plusOne([1, 2, 3])
    print(res)

    res = Solution().plusOne([4, 3, 2, 1])
    print(res)

    res = Solution().plusOne([9])
    print(res)


    res = Solution().plusOne([8, 9, 9, 9])
    print(res)