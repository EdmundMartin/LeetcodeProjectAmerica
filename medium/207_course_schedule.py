from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqs = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preqs[course].append(pre)

        visited = set()

        def depth_first_search(course):
            if course in visited:
                return False
            if not preqs[course]:
                return True
            visited.add(course)
            for pre in preqs[course]:
                if depth_first_search(pre) is False:
                    return False
            visited.remove(course)
            preqs[course] = []
            return True

        for course in range(numCourses):
            if not depth_first_search(course):
                return False
        return True





