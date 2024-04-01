from collections import defaultdict


# 51ms - Beats 92.24%of users with Python3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        left = 0
        max_size = 0
        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            max_size = max(max_size, right - left + 1)
        return max_size


if __name__ == '__main__':
    res = Solution().lengthOfLongestSubstring("abcabcbb")
    print(res)

    res = Solution().lengthOfLongestSubstring("bbbbb")
    print(res)

    res = Solution().lengthOfLongestSubstring("pwwkew")
    print(res)
