from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        new_code = []
        if k > 0:
            for idx in range(len(code)):
                new_num = 0
                for i in range(1, k + 1):
                    new_idx = idx + i
                    if new_idx >= len(code):
                        new_idx = new_idx % len(code)
                    new_num += code[new_idx]
                new_code.append(new_num)
        else:
            k = abs(k)
            for idx in range(len(code)):
                new_num = 0
                for i in range(1, k + 1):
                    new_idx = idx - i
                    new_num += code[new_idx]
                new_code.append(new_num)
        return new_code


if __name__ == '__main__':
    res = Solution().decrypt([5,7,1,4], 3)

    res = Solution().decrypt([2,4,9,3], -2)
    print(res)

