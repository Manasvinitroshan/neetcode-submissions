class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0 
        curr = 0
        answer = 0 
        hashmap = set()
        for right in range(len(s)):
            
            while(s[right] in hashmap):
                hashmap.remove(s[left])
                left+=1
            
            curr = max(curr, right - left + 1)

            hashmap.add(s[right])

            

        return curr
        
        


        