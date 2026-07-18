class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0]) #x is the array, array[0] is start time and we are sorting by the start time

        res = []

        for s,e in intervals:
            if e < newInterval[0]:
                res.append([s,e])
            
            elif s > newInterval[1]:
                res.append(newInterval)
                newInterval = [s,e]
            
            else:
                newInterval[0] = min(newInterval[0],s)
                newInterval[1] = max(newInterval[1],e)

            
        res.append(newInterval)

        return res

            
        