class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False

        

        freq = [0]*26

        for c in s:
            freq[ord(c)-ord('a')]+=1
        

        for char in t:
            freq[ord(char) - ord('a')]-=1
        


        for val in freq:

            if val!=0:
                return False


        
        return True

      
        