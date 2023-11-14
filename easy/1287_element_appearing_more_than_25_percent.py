from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        last_char = arr[0]
        count = 1

        qualifier = len(arr) // 4

        for char in arr[1:]:
            if count > qualifier:
                return last_char

            if char != last_char:
                last_char = char
                count = 1
            else:
                count += 1
        if count > qualifier:
            return last_char


if __name__ == '__main__':
    res = Solution().findSpecialInteger([1, 2, 3, 3])
    print(res)