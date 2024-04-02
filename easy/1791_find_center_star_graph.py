from typing import List
from collections import defaultdict


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        mapping = defaultdict(list)

        for edge in edges:
            mapping[edge[0]].append(edge[1])
            mapping[edge[1]].append(edge[0])
        n = len(mapping) - 1
        for k, v in mapping.items():
            if len(v) == n:
                return k



if __name__ == '__main__':
    res = Solution().findCenter([[1,2], [2,3], [4,2]])
    print(res)

    res = Solution().findCenter([[1,2],[5,1],[1,3],[1,4]])
    print(res)