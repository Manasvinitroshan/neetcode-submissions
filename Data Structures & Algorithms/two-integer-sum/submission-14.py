class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i,n in enumerate(nums):
            comp = target - nums[i] 

            if comp in hashmap:
                return [hashmap[comp],i]

            hashmap[n] = i
        

        return [-1,-1]