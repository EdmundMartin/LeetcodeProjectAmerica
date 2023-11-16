from typing import List


def count_in_str(target: str, value: str):
    count = 0
    for t in target:
        if t == value:
            count += 1
    return count


def calculate_truck_time(truck, garbage, time):
    last_idx = -1
    for idx, g in enumerate(garbage):
        if truck in g:
            last_idx = idx
    if last_idx == -1:
        return 0

    time_idx = 0
    total = 0
    for i in range(last_idx + 1):
        total += count_in_str(garbage[i], truck)

        if i == 0:
            continue
        total += time[time_idx]
        time_idx += 1
    return total


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = 0
        res += calculate_truck_time("P", garbage, travel)
        res += calculate_truck_time("G", garbage, travel)
        res += calculate_truck_time("M", garbage, travel)

        return res


if __name__ == '__main__':
    Solution().garbageCollection(["G", "M"], [1])
