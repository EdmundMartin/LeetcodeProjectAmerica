

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap = dict()
        tMap = dict()

        for idx in range(len(s)):
            sChar = s[idx]
            tChar = t[idx]

            if sChar in sMap and sMap[sChar] != tChar:
                return False
            if tChar in tMap and tMap[tChar] != sChar:
                return False
            sMap[sChar] = tChar
            tMap[tChar] = sChar
        return True