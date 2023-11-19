from typing import List


def count_row(row: str):
    return sum([1 for i in row if i == "1"])


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        last_row_count = 0
        total = 0
        for row in bank:
            current_count = count_row(row)
            if last_row_count != 0:
                total += last_row_count * current_count
            if current_count != 0:
                last_row_count = current_count
        return total


if __name__ == '__main__':
    res = Solution().numberOfBeams(["011001","000000","010100","001000"])
    print(res)

    res = Solution().numberOfBeams(["000","111","000"])
    print(res)