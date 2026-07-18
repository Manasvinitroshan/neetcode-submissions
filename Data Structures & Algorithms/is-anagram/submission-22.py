class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = [0]*26

        if len(s)!=len(t):
            return False


        for i in range(len(s)):
            freq[ord(s[i]) - ord('a')]+=1


        for j in range(len(t)):
            freq[ord(t[j]) - ord('a')]-=1

        

        for val in freq:
            if val!=0:
                return False


        return True
        