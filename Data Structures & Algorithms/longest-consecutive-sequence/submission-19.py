class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        ans = 0
        if len(nums) == 0:
            return 0

        
        start = nums[0]

        for num in num_set:
            if num-1 not in num_set:
                start = num

            streak = 1
            while start+1 in num_set:
                streak+=1
                start = start+1
            
            ans = max(ans,streak)

        return ans

            

        