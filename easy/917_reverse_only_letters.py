

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        output = ["" for _ in s]
        rev_chars = []
        for idx, ch in enumerate(s):
            if ch.isalpha():
                rev_chars.append(ch)
            else:
                output[idx] = ch
        idx = 0
        while rev_chars:
            if output[idx] != "":
                idx += 1
            else:
                output[idx] = rev_chars.pop(-1)
        return "".join(output)






if __name__ == '__main__':
    res = Solution().reverseOnlyLetters("ab-cd")
    print(res)

    res = Solution().reverseOnlyLetters("a-bC-dEf-ghIj")
    print(res)