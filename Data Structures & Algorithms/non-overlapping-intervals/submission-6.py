class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])

        ans = 0
        end = float('-inf')
        for s,e in intervals:
            if end <= s:
                end = e
                
            
            else:
                ans+=1
                continue
                
        
        return ans


        