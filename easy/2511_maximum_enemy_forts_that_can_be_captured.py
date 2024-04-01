from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:

        empty_slot = False
        captured = 0
        for idx in range(len(forts) - 1, -1, -1):
            if forts[idx] == -1:
                empty_slot = True
            elif forts[idx] == 1:
                empty_slot = False
            elif empty_slot and forts[idx] == 0:
                captured += 1
        return captured
