
class Solution:
    def interpret(self, command: str) -> str:
        output = ""
        idx = 0
        while idx < len(command):
            current_char = command[idx]
            if current_char == "(":
                next_char = command[idx + 1]
                if next_char == ")":
                    output += "o"
                    idx += 2
                else:
                    output += "al"
                    idx += 4
            else:
                output += command[idx]
                idx += 1
        return output


if __name__ == '__main__':
    res = Solution().interpret("G()(al)")
    print(res)