from collections import defaultdict


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        counter = defaultdict(int)
        max_num = 1
        for row in grid:
            for item in row:
                counter[item] += 1
                max_num += 1
        result = [None, None]
        for i in range(1, max_num):
            if counter[i] > 1:
                result[0] = i
                if result[1]:
                    return result
            if counter[i] == 0:
                result[1] = i
                if result[0]:
                    return result
        return result