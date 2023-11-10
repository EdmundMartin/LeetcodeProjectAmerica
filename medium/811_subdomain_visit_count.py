from typing import List
from collections import defaultdict


def display_results(results):
    res = []
    for key, value in results.items():
        res.append(f"{value} {key}")
    return res


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        results = defaultdict(int)

        for domain in cpdomains:
            count, domain = domain.split(' ')
            count = int(count)
            results[domain] += count

            while "." in domain:
                domain = ".".join(domain.split(".")[1:])
                results[domain] += count
        return display_results(results)


if __name__ == '__main__':
    out = Solution().subdomainVisits(["9001 discuss.leetcode.com"])
    print(out)