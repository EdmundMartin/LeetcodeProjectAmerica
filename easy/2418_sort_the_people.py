from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = sorted([(h, idx) for idx, h in enumerate(heights)], reverse=True)
        return [
            names[idx] for _, idx in res
        ]


if __name__ == '__main__':
    Solution().sortPeople(["Mary", "John", "Emma"], [180, 165, 170])
