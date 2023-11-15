

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = []
        for char in s:
            if char != "-":
                chars.append(char.upper())
        parts = []
        while len(chars) >= k:
            part = ''.join(chars[-k:])
            chars = chars[:-k]
            parts.insert(0, part)
        if len(chars) > 0:
            parts.insert(0, ''.join(chars))
        return '-'.join(parts)


if __name__ == '__main__':
    res = Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4)
    print(res)