from typing import List


def append_count(count: int, target):
    if count <= 1:
        return
    temp = []
    while count >= 10:
        remainder = count % 10
        count //= 10
        temp.append(f"{remainder}")
    target.append(f"{count}")
    for i in temp[::-1]:
        target.append(i)


class Solution:
    def compress(self, chars: List[str]) -> int:

        output = [

        ]
        last_char = None
        count = 0

        for char in chars:
            if char != last_char:
                if last_char:
                    output.append(last_char)
                    append_count(count, output)
                last_char = char
                count = 1
            else:
                count += 1
        output.append(last_char)
        append_count(count, output)

        for idx in range(len(output)):
            if idx >= len(chars):
                chars.append(output[idx])
            else:
                chars[idx] = output[idx]
        return len(output)


if __name__ == '__main__':
    Solution().compress(["a","a","b","b","c","c","c"])