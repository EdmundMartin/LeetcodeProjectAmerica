from typing import List

from collections import defaultdict


class SolutionSlow:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        student_counter = defaultdict(int)
        for start, end in zip(startTime, endTime):
            for i in range(start, end + 1):
                student_counter[i] += 1
        return student_counter[queryTime]


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for start, end in zip(startTime, endTime):
            if start <= queryTime and end >= queryTime:
                count += 1
        return count