class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        res = 0
        ans = 0
        hashmap = {}
        most = 0
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r],0)
            most = max(most,hashmap[s[r]])

            while (r-l+1) - most > k:
                hashmap[s[l]]-=1
                if hashmap[s[l]] == 0:
                    del hashmap[s[l]]

                l+=1
            
            res = r-l+1
            ans = max(ans,res)


        return ans
            

        