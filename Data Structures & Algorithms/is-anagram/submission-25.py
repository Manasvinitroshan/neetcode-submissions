class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = [0]*26

        if len(s)!= len(t):
            return False

        
        for char in s:
            freq[ord(char) - ord('a')]+=1


        for char2 in t:
            freq[ord(char2) - ord('a')]-=1
        
        for val in freq:
            if val!=0:
                return False


        return True

        