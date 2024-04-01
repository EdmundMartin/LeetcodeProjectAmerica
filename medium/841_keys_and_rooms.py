from typing import List


def depth_first_search(rooms, visited, keys: List[int]):
    for key in keys:
        if visited[key] is True:
            continue
        visited[key] = True
        depth_first_search(rooms, visited, rooms[key])


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = [False] * len(rooms)
        visited[0] = True

        depth_first_search(rooms, visited, rooms[0])
        return all([v for v in visited])


if __name__ == '__main__':
    Solution().canVisitAllRooms([[1], [2], [3], []])
