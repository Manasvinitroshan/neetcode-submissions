class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        for i,a in enumerate(nums):

            if i > 0 and a == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1

            while l < r:
                total = nums[i]+nums[l]+nums[r]

                if total == 0:
                    res.append([a,nums[l],nums[r]])
                    r-=1
                    l+=1
                    while l < r and nums[r+1] == nums[r]:
                        r-=1
                   
                
                elif total > 0:
                    r-=1
                    
                else:
                    l+=1
                    

            

                
        return res
        