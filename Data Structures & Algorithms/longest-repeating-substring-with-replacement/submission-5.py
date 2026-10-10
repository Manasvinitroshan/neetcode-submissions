class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        hashmap = {}
        ans = 0
        max_freq = 0


        for r in range(len(s)):


            hashmap[s[r]] = 1 + hashmap.get(s[r],0)
            max_freq = max(max_freq, hashmap[s[r]])

            while ((r - l + 1) - max_freq) > k:
                hashmap[s[l]]-=1

                if hashmap[s[l]] == 0:
                    del hashmap[s[l]]

                
                l+=1
            
            ans = max(ans,r-l+1)
        
        return ans
