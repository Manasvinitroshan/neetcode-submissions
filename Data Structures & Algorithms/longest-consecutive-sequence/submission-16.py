class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        longest = 0


        for num in nums:
            if num-1 not in s:
                start = num
                streak = 0

                while start in s:
                    streak+=1
                    start+=1

                longest = max(longest,streak)

        return longest

        
        