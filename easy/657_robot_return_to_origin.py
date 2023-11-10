

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start = [0, 0]

        for move in moves:
            if move == "U":
                start[0] += 1
            if move == "D":
                start[0] -= 1
            if move == "L":
                start[1] -= 1
            if move == "R":
                start[1] += 1
        return start == [0, 0]