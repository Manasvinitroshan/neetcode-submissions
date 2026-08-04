class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashmap = {}
        res = 0
        l = 0
        ans = 0

        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r],0)

            while hashmap[s[r]] > 1:
                hashmap[s[l]]-=1
                if hashmap[s[l]] == 0:
                    del hashmap[s[l]]
                
                l+=1
        
            res = r-l+1
            ans = max(ans,res)

        return ans


            
        