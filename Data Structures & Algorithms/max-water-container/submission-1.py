class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        r = len(heights) - 1
        res = 0

        while l < r:
            w = r - l
            h = min(heights[l],heights[r])
            area = w*h

            if(heights[r] > heights[l]):
                l+=1
            elif(heights[r] < heights[l]):
                r-=1
            else:
                r-=1

            res = max(res,area)

        return res
            


        