from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        prev_scores = []
        for idx, op in enumerate(operations):
            if op.isnumeric() or op[0] == "-":
                total += int(op)
                prev_scores.append(int(op))
            if op == '+':
                total += sum(prev_scores[-2:])
                prev_scores.append(sum(prev_scores[-2:]))
            if op == 'D':
                total += prev_scores[-1] * 2
                prev_scores.append(prev_scores[-1] * 2)
            if op == 'C':
                total -= prev_scores[-1]
                prev_scores = prev_scores[:-1]
        return total


if __name__ == '__main__':
    res = Solution().calPoints(["5","-2","4","C","D","9","+","+"])
    print(res)
