from collections import defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = defaultdict(int)
        for ch in s:
            counter[ch] += 1
        result = ""
        while counter:
            max_value = max(counter.values())
            keys = counter.keys()
            to_delete = []
            for key in keys:
                if counter[key] == max_value:
                    result += key * max_value
                    to_delete.append(key)
            for k in to_delete:
                del counter[k]
        return result


if __name__ == '__main__':
    res = Solution().frequencySort("tree")
    print(res)