class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        
        for a in strs:
            count = [0]*26
            for i in range(len(a)):

                count[ord(a[i])-ord('a')]+=1
        
            res[tuple(count)].append(a)
        
        return list(res.values())
        
            
        