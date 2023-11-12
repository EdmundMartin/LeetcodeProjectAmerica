from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        people_trust = dict()
        for i in range(1, n +1):
            people_trust[i] = []

        for trusting in trust:
            person, trustee = trusting
            people_trust[person].append(trustee)

        potential_judges = []
        for p, trusts in people_trust.items():
            if len(trusts) == 0:
                potential_judges.append(p)
        if len(potential_judges) == 0:
            return -1
        if len(potential_judges) > 1:
            return -1

        candidate = potential_judges[0]
        for p, trusts in people_trust.items():
            if p == candidate:
                continue
            if candidate not in trusts:
                return -1
        return candidate


if __name__ == '__main__':
    res = Solution().findJudge(2, [[1, 2]])
    print(res)

    res = Solution().findJudge(3, [[1,3],[2,3]])
    print(res)