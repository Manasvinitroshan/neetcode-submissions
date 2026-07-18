class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        s = set(nums)
        longest = 0
        start = 0

        for num in s:

            if num-1 not in s:
                start = num

                streak = 0
                while start in s:
                    start+=1
                    streak+=1

            
                longest = max(longest,streak)


        return longest
        