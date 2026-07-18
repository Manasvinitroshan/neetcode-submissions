class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

    
        
        intervals.sort(key=lambda x: x[1])
        i = 0
        count = 0

        for j in range(1,len(intervals)):

            if intervals[j][0] >= intervals[i][1]:
                i=j

            else:
                count+=1

        return count


        