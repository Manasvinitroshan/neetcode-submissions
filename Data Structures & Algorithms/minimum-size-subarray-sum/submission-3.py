class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        ans = float("inf")
        curr = 0

        for r in range(len(nums)):

            curr+=nums[r]

            while curr >= target:
                ans = min(ans,r-l+1)
                curr-=nums[l]
                l+=1
            


        return ans if ans!= float("inf") else 0

        