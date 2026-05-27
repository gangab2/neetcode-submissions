class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d1 = {}
        d2 = {}

        for e1 in s:
            d1[e1] = d1.get(e1, 0) + 1
        for e2 in t:
            d2[e2] = d2.get(e2, 0) + 1
        
        return d1 == d2 



        