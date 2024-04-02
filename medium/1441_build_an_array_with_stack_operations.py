from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target = set(target)
        max_num = max(target)
        result = []
        for i in range(1, min(n + 1, max_num + 1)):
            if i in target:
                result.append("Push")
            else:
                result.extend(["Push", "Pop"])
        return result


if __name__ == '__main__':
    res = Solution().buildArray([1, 3], 3)
    print(res)

    res = Solution().buildArray([1, 2, 3], 3)
    print(res)

    res = Solution().buildArray([1, 2], 4)
    print(res)