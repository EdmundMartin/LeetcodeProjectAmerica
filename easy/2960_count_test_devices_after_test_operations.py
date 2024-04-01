from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count = 0
        for idx in range(len(batteryPercentages)):

            if batteryPercentages[idx] > 0:
                count += 1

                for j in range(idx + 1, len(batteryPercentages)):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
        return count