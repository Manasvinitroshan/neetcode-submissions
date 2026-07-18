class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        h1 = {}
        h2 = {}

        for c in s:
            h1[c] = h1.get(c, 0) + 1
        
        for x in t:
            h2[x] = h2.get(x, 0) + 1
        
        return h1 == h2
