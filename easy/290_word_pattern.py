

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapping_pattern_to_animal = {}
        animal_to_pattern = {}

        if len(pattern) != len(s.split(" ")):
            return False

        for idx, content in enumerate(s.split(" ")):
            try:
                pattern_key = pattern[idx]
            except IndexError:
                return False
            if content not in animal_to_pattern:
                animal_to_pattern[content] = pattern_key
            if pattern_key not in mapping_pattern_to_animal:
                mapping_pattern_to_animal[pattern_key] = content

            if animal_to_pattern[content] != pattern_key:
                return False
            if mapping_pattern_to_animal[pattern_key] != content:
                return False
        return True


if __name__ == '__main__':
    res = Solution().wordPattern("abba", "dog cat cat fish")
    print(res)