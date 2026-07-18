class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = [0]*26

        if len(s) != len(t):
            return False

        
        for c in s:
            freq[ord(c)-ord('a')]+=1

        
        for c1 in t:
            freq[ord(c1)-ord('a')]-=1

        
        for num in freq:
            if num!=0:
                return False

        
        return True
            

















        