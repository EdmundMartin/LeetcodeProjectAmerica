from typing import List
from collections import defaultdict


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        count_els = defaultdict(int)
        for item in arr1:
            count_els[item] += 1

        output_array = []
        for item in arr2:
            if item in count_els:
                for i in range(count_els[item]):
                    output_array.append(item)
                del count_els[item]

        for value in sorted(count_els.keys()):
            for i in range(count_els[value]):
                output_array.append(value)
        return output_array



if __name__ == '__main__':
    res = Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6])