from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        index = {
            "type": 0,
            "color": 1,
            "name": 2,
        }
        for item in items:
            raw_value = item[index[ruleKey]]
            if raw_value == ruleValue:
                count += 1
        return count
