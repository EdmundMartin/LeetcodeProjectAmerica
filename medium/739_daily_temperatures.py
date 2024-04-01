from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        output = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):

            if len(stack) > 0:
                while stack and stack[-1][0] < temp:
                    out_idx = stack[-1][1]
                    output[out_idx] = idx - out_idx
                    stack.pop(-1)
            stack.append((temp, idx))
        return output


if __name__ == '__main__':
    res = Solution().dailyTemperatures([30, 60, 90])
    print(res)

    res = Solution().dailyTemperatures([73,74,75,71,69,72,76,73])
    print(res)