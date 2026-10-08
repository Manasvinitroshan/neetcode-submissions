class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a:
                continue

            for j in range(i+1,len(nums)):

                if j > i+1 and nums[j-1] == nums[j]:
                    continue

                
                l = j+1
                r = len(nums)-1


                while l < r:
                    if (a+nums[j]+nums[l]+nums[r]) == target:
                        res.append([a,nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1

                        while l < r and nums[l-1] == nums[l]:
                            l+=1
                    
                    elif (a+nums[j]+nums[l]+nums[r]) < target:
                        l+=1
                    else:
                        r-=1


        return res


            
            

        
        