class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        dic1 = {}
        if len(s) != len(t):
            return False
        for n in s:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
        for x in t:
            if x not in dic1:
                dic1[x] = 1
            else:
                dic1[x] += 1
        return dic == dic1