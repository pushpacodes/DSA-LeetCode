class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sf = [0] * 26
        tf = [0] * 26
        for i in s:
            sf[ord(i) - 97] += 1
        for j in t:
            tf[ord(j) - 97] += 1
        return sf == tf
