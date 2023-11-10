from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        idx = 0
        while idx < len(s) / 2:
            s[idx], s[-(idx + 1)] = s[-(idx +1)], s[idx]
            idx += 1


if __name__ == '__main__':
    input_list = ["h", "e", "l", "l", "o"]
    Solution().reverseString(input_list)
    print(input_list)