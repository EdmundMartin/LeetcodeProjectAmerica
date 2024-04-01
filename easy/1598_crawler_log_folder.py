from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0

        for log in logs:
            if log == "../" and depth > 0:
                depth -= 1
            elif log == "../":
                continue
            elif log == "./":
                continue
            else:
                depth += 1
        return depth


if __name__ == '__main__':
    res = Solution().minOperations(["./","../","./"])
    print(res)