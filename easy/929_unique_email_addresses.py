from typing import List


def split_user(user: str):
    alternate = ""
    for idx, ch in enumerate(user):
        if ch == "+":
            return alternate
        if ch == ".":
            continue
        alternate += ch
    return alternate


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            parts = email.split('@')
            user, domain = parts[0], parts[1]
            user = split_user(user)
            new_email = f"{user}@{domain}"
            seen.add(new_email)
        return len(seen)


if __name__ == '__main__':
    res = Solution().numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
    print(res)