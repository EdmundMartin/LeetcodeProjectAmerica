

class Solution:
    def reformatNumber(self, number: str) -> str:
        just_numbers = ""
        for char in number:
            if char.isnumeric():
                just_numbers += char
        result = ""
        while len(just_numbers) > 4:
            numbers = just_numbers[:3]
            just_numbers = just_numbers[3:]
            result += f"{numbers}-"
        if len(just_numbers) == 4:
            result += f"{just_numbers[:2]}-{just_numbers[2:]}"
            just_numbers = ""
        if len(just_numbers) > 0:
            result += f"{just_numbers}"
        if result[-1] == "-":
            return result[:-1]
        return result


if __name__ == '__main__':
    Solution().reformatNumber("1-23-45 6")