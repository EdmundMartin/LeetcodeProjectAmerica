

class Solution:
    def sortVowels(self, s: str) -> str:

        vowels = {'a', 'e', 'i', 'o', 'u'}

        results = []
        swap_indexes = set()
        for idx, char in enumerate(s):
            if char.lower() in vowels:
                results.append((ord(char), char))
                swap_indexes.add(idx)
        results = sorted(results)
        output = ""
        for idx, char in enumerate(s):
            if idx in swap_indexes:
                details = results.pop(0)
                output += details[1]
            else:
                output += char
        return output


if __name__ == '__main__':
    res = Solution().sortVowels("lEetcOde")
    print(res)