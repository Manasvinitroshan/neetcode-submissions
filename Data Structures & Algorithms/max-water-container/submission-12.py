class Solution:
    def maxArea(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)-1
        res = 0
        area = 0

        while l < r:
            lenght = r-l
            h = min(nums[r],nums[l])

            if(nums[l] < nums[r]):
                l+=1
            else:
                r-=1

            
            area = h*lenght

            res = max(res,area)

        
        return res
            
            


        