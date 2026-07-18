class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        res = 0

        r = len(heights) -1

        while l < r:
            h = min(heights[r],heights[l])
            leng = r-l

            area = h*leng

            res = max(res,area)


            if heights[r] < heights[l]:
                r-=1

            else:
                l+=1

        
        return res

        
        